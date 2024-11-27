import unittest
from unittest.mock import MagicMock, patch

# Importa o código do sensor
import dhtSensor

class TestDHTSensor(unittest.TestCase):
    @patch('dhtSensor.network.WLAN')
    @patch('dhtSensor.Pin')
    @patch('dhtSensor.dht.DHT11')
    def test_wifi_connection(self, mock_DHT11, mock_Pin, mock_WLAN):
        # Mock do Wi-Fi
        mock_wlan_instance = MagicMock()
        mock_WLAN.return_value = mock_wlan_instance
        mock_wlan_instance.isconnected.return_value = True

        # Executa a conexão ao Wi-Fi
        dhtSensor.connect_to_wifi()

        # Verifica se o Wi-Fi foi ativado e conectado
        mock_wlan_instance.active.assert_called_with(True)
        mock_wlan_instance.connect.assert_called_with('TesteWiFi', 'SenhaFicticia123')
        mock_wlan_instance.isconnected.assert_called()

    @patch('dhtSensor.time.sleep', return_value=None)  # Evita delays durante o teste
    @patch('dhtSensor.dht.DHT11')
    @patch('dhtSensor.Pin')
    def test_sensor_reading(self, mock_Pin, mock_DHT11, mock_sleep):
        # Mock do sensor DHT11
        mock_dht_instance = MagicMock()
        mock_DHT11.return_value = mock_dht_instance
        mock_dht_instance.temperature.return_value = 22.5  # Valor fictício de temperatura
        mock_dht_instance.humidity.return_value = 55.0  # Valor fictício de umidade

        # Simula a leitura do sensor
        dhtSensor.dht_sensor.measure()
        temperature = dhtSensor.dht_sensor.temperature()
        humidity = dhtSensor.dht_sensor.humidity()

        # Verifica se os valores retornados são os esperados
        self.assertEqual(temperature, 22.5)
        self.assertEqual(humidity, 55.0)

if __name__ == '__main__':
    unittest.main()
