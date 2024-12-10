import machine
import time
from machine import Pin, ADC
import dht
import tensorflow as tf

dht_sensor = dht.DHT11(Pin(2))
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)

interpreter = tf.lite.Interpreter(model_path="modelo_plantio.tflite")
interpreter.allocate_tensors()

def predict_conditions(temperature, humidity, light_value):
    input_data = [[temperature, humidity, light_value]]
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])[0][0]
    return "Bom para plantio" if prediction >= 0.5 else "Não adequado"

while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        light_value = light_sensor.read()
        status = predict_conditions(temperature, humidity, light_value)
        print(f"Temperatura: {temperature}°C, Umidade: {humidity}%, Luminosidade: {light_value}")
        print(f"Condição: {status}")
        with open("dados_plantio.csv", "a") as f:
            f.write(f"{temperature},{humidity},{light_value},{status}\n")
        time.sleep(5)
    except Exception as e:
        print("Erro ao coletar dados:", e)
        time.sleep(5)
