import machine
import time
import network
from machine import Pin, ADC

# Configurações do Wi-Fi 
SSID = 'NET_VIRTUA_5G'  
PASSWORD = '4788135267'  

# Conecta ao Wi-Fi (pode ser comentado se não for usar)
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        time.sleep(1)
    print('Conectado a', SSID)

# Configuração do sensor de luminosidade
light_sensor = ADC(Pin(34))  # Pino onde o sensor de luminosidade está conectado
light_sensor.atten(ADC.ATTN_11DB)  # Configuração para ler tensões maiores

# Loop principal
connect_to_wifi()  # Comente esta linha se não for usar Wi-Fi

while True:
    light_value = light_sensor.read()  # Lê o valor do sensor de luminosidade
    
    # Se não houver leitura, use valor fictício
    if light_value is None:
        light_value = 0  # Valor fictício para luminosidade

    print('Luminosidade:', light_value)

    time.sleep(5)  # Espera 5 segundos antes da próxima leitura
