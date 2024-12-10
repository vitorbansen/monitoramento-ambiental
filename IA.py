import machine
import time
from machine import Pin, ADC
import dht

# Configuração do sensor DHT11
dht_sensor = dht.DHT11(Pin(2))
light_sensor = ADC(Pin(34))  # Sensor de luminosidade
light_sensor.atten(ADC.ATTN_11DB)

# Função para avaliar condições de plantio usando lógica fuzzy simples
def fuzzy_evaluation(temperature, humidity, light_value):
    
    if temperature < 20:
        temp_score = "Baixa"
    elif 20 <= temperature <= 30:
        temp_score = "Ideal"
    else:
        temp_score = "Alta"

    
    if humidity < 50:
        humidity_score = "Baixa"
    elif 50 <= humidity <= 70:
        humidity_score = "Ideal"
    else:
        humidity_score = "Alta"

    
    if light_value < 2000:
        light_score = "Baixa"
    else:
        light_score = "Boa"

    
    if temp_score == "Ideal" and humidity_score == "Ideal" and light_score == "Boa":
        return "Bom para plantio"
    else:
        return "Não adequado"


while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        light_value = light_sensor.read()

        # Avaliação fuzzy
        status = fuzzy_evaluation(temperature, humidity, light_value)

        print(f"Temperatura: {temperature}°C, Umidade: {humidity}%, Luminosidade: {light_value}")
        print(f"Condição: {status}")

        
        with open("dados_plantio.csv", "a") as f:
            f.write(f"{temperature},{humidity},{light_value},{status}\n")

        time.sleep(5)

    except Exception as e:
        print("Erro ao coletar dados:", e)
        time.sleep(5)
