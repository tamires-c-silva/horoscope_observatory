import  abc
import re
from unittest import mock
from mock import call
from horoscope_observatory.horoscope_load import HoroscopeLoad
import pytest
from unittest import TestCase
from unittest.mock import *
import requests 

class TestHoroscopeLoad(TestCase):
    
    def test_if_load_method_calls_kafkahook(self):
        with patch('kafka.kafka_hook.KafkaHook.process_kafka') as mock_process_kafka:                                                                                                                                                                       
            load_class = HoroscopeLoad()                                                                                                                                                                                            
            load_class.load(transformed_data="data")                                                                                                                                                                                            
            mock_process_kafka.assert_called_once()