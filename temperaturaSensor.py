import machine
import time
import network
from machine import Pin
import dht

# Configurações do Wi-Fi 
SSID = 'TesteWiFi'  
PASSWORD = 'SenhaFicticia123'  

# Conecta ao Wi-Fi (pode ser comentado se não for usar)
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        time.sleep(1)
    print('Conectado a', SSID)

# Configuração do sensor DHT11
dht_sensor = dht.DHT11(Pin(2))  # Pino onde o sensor está conectado

# Loop principal
connect_to_wifi()  # Comente esta linha se não for usar Wi-Fi

while True:
    dht_sensor.measure()  # Realiza a medição
    temperature = dht_sensor.temperature()  # Obtém a temperatura
    humidity = dht_sensor.humidity()  # Obtém a umidade
    
    # Se não houver leitura, use valores fictícios
    if temperature is None:
        temperature = 25.0  # Valor fictício para temperatura
    if humidity is None:
        humidity = 60.0  # Valor fictício para umidade

    print('Temperatura:', temperature, '°C')
    print('Umidade:', humidity, '%')

    time.sleep(5)  # Espera 5 segundos antes da próxima leitura
