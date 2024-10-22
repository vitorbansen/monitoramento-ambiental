import unittest
from unittest.mock import patch
from sensor import DHTSensor  # Substitua pelo nome correto do seu módulo

class TestDHTSensor(unittest.TestCase):
    
    @patch('sensor.dht.DHT11')
    def test_temperature_reading(self, MockDHT):
        sensor = DHTSensor()
        MockDHT.return_value.temperature.return_value = 25  # Simulando temperatura de 25°C
        temperature = sensor.read_temperature()
        self.assertEqual(temperature, 25)

    @patch('sensor.dht.DHT11')
    def test_humidity_reading(self, MockDHT):
        sensor = DHTSensor()
        MockDHT.return_value.humidity.return_value = 60  # Simulando umidade de 60%
        humidity = sensor.read_humidity()
        self.assertEqual(humidity, 60)

    @patch('sensor.dht.DHT11')
    def test_reading_with_fallback(self, MockDHT):
        sensor = DHTSensor()
        MockDHT.return_value.temperature.return_value = None  # Simulando falha na leitura
        MockDHT.return_value.humidity.return_value = None  # Simulando falha na leitura

        temperature = sensor.read_temperature()
        humidity = sensor.read_humidity()

        # Verifica se os valores fictícios foram usados
        self.assertEqual(temperature, 25.0)
        self.assertEqual(humidity, 60.0)

if __name__ == '__main__':
    unittest.main()
