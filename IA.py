import machine
import time
from machine import Pin, ADC
import dht

# Configuração do sensor DHT11
dht_sensor = dht.DHT11(Pin(2))
light_sensor = ADC(Pin(34))  # Sensor de luminosidade
light_sensor.atten(ADC.ATTN_11DB)

# Função para verificar condições de plantio
def is_good_for_planting(temperature, humidity, light_value):
    # Condições ideais iniciais
    if 20 <= temperature <= 30 and 50 <= humidity <= 70 and light_value >= 2000:
        return "Bom para plantio"
    return "Não adequado"

# Loop principal
while True:
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    light_value = light_sensor.read()

    status = is_good_for_planting(temperature, humidity, light_value)

    print(f"Temperatura: {temperature}°C, Umidade: {humidity}%, Luminosidade: {light_value}")
    print(f"Condição: {status}")

    # Simule envio para um servidor ou salve os dados localmente
    # Exemplo: salvar em arquivo
    with open("dados_plantio.csv", "a") as f:
        f.write(f"{temperature},{humidity},{light_value},{status}\n")

    time.sleep(5)
