import  abc
import json
import re
from unittest import mock

from mock import call
import pandas
from horoscope_observatory.horoscope_transform import HoroscopeTransform
import pytest
from unittest import TestCase
from unittest.mock import *
import requests 

class TestHoroscopeLoad(TestCase):
    
    def test_if_convert_dict_to_list_of_dict(self):
        transform_class = HoroscopeTransform()
        result = transform_class.convert_dict_to_list_of_dict(
            row = {"exciting":["anticipation","joy","positive","surprise"],"forward":["positive"],"interesting":["positive"],"offer":["positive"],"show":["trust"]}, 
            key_name="word", 
            value_name="emotion")
        expected = [{'word': 'exciting', 'emotion': ['anticipation', 'joy', 'positive', 'surprise']}, 
                    {'word': 'forward', 'emotion': ['positive']}, 
                    {'word': 'interesting', 'emotion': ['positive']}, 
                    {'word': 'offer', 'emotion': ['positive']}, 
                    {'word': 'show', 'emotion': ['trust']}]
        
        assert expected == result
    

    def test_if_feeling_analysis_is_happening(self):
        transform_class = HoroscopeTransform()
        content = json.loads(b'{"date_range": "Jun 22 - Jul 22", "current_date": "May 23, 2022", "description": "You\'ve got tons of exciting company to look forward to, starting today. Listen up for anyone with an interesting accent, and don\'t hesitate to offer to show them around.", "compatibility": "Sagittarius", "mood": "Happy", "color": "Purple", "lucky_number": "18", "lucky_time": "11am"}\n')
        dataframe = pandas.DataFrame(content, index=[0]).reset_index()
        result = transform_class.analyse_feeling(dataframe)
        result_json = result.to_json()
        expected = """{"index":{"0":0},"date_range":{"0":"Jun 22 - Jul 22"},"current_date":{"0":"May 23, 2022"},"description":{"0":"You've got tons of exciting company to look forward to, starting today. Listen up for anyone with an interesting accent, and don't hesitate to offer to show them around."},"compatibility":{"0":"Sagittarius"},"mood":{"0":"Happy"},"color":{"0":"Purple"},"lucky_number":{"0":"18"},"lucky_time":{"0":"11am"},"feeling_analysis_affect_dict":{"0":[{"word":"exciting","feelings":["anticipation","joy","positive","surprise"]},{"word":"forward","feelings":["positive"]},{"word":"interesting","feelings":["positive"]},{"word":"offer","feelings":["positive"]},{"word":"show","feelings":["trust"]}]}}"""
       
        assert expected == result_json
     
    @mock.patch('horoscope_observatory.horoscope_transform.HoroscopeTransform.create_dataframe_using_extracted_data')   
    def test_if_dataframe_creation_is_called(self, create_df_mock):
        content = json.loads(b'{"date_range": "Jun 22 - Jul 22", "current_date": "May 23, 2022", "description": "You\'ve got tons of exciting company to look forward to, starting today. Listen up for anyone with an interesting accent, and don\'t hesitate to offer to show them around.", "compatibility": "Sagittarius", "mood": "Happy", "color": "Purple", "lucky_number": "18", "lucky_time": "11am"}\n')
        dataframe = pandas.DataFrame(content, index=[0])
        transform_class = HoroscopeTransform()
        transform_class.transform(dataframe)
        
        create_df_mock.return_value = Mock(extracted_data=dataframe)
        