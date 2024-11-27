import unittest
from unittest.mock import MagicMock, patch

# Importa o código do sensor
import luminosidadeSensor

class TestLuminosidadeSensor(unittest.TestCase):
    @patch('luminosidadeSensor.network.WLAN')
    @patch('luminosidadeSensor.ADC')
    @patch('luminosidadeSensor.Pin')
    def test_wifi_connection(self, mock_Pin, mock_ADC, mock_WLAN):
        # Mock do Wi-Fi
        mock_wlan_instance = MagicMock()
        mock_WLAN.return_value = mock_wlan_instance
        mock_wlan_instance.isconnected.return_value = True

        # Executa a conexão ao Wi-Fi
        luminosidadeSensor.connect_to_wifi()

        # Verifica se o Wi-Fi foi ativado e conectado
        mock_wlan_instance.active.assert_called_with(True)
        mock_wlan_instance.connect.assert_called_with('TesteWiFi', 'SenhaFicticia123')
        mock_wlan_instance.isconnected.assert_called()

    @patch('luminosidadeSensor.time.sleep', return_value=None)  # Evita delays durante o teste
    @patch('luminosidadeSensor.ADC')
    @patch('luminosidadeSensor.Pin')
    def test_sensor_reading(self, mock_Pin, mock_ADC, mock_sleep):
        # Mock do sensor de luminosidade
        mock_adc_instance = MagicMock()
        mock_ADC.return_value = mock_adc_instance
        mock_adc_instance.read.return_value = 1234  # Valor fictício de leitura

        # Leitura do sensor
        light_value = luminosidadeSensor.light_sensor.read()

        # Verifica se o sensor leu o valor esperado
        self.assertEqual(light_value, 1234)

if __name__ == '__main__':
    unittest.main()
