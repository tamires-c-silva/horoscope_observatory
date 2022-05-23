import  abc
import json
import re
from typing import Dict
from unittest import mock

from mock import call
from horoscope_observatory.horoscope_extract import HoroscopeExtract
import pytest
from unittest import TestCase
from unittest.mock import *

class TestHoroscopeExtract(TestCase):
    
    def test_if_extract_method_is_creating_api_endpoint_correctly(self):
        extract_class = HoroscopeExtract()
        result = extract_class.format_api_endpoint(sign='cancer', day='today')
        endpoint= (f'https://aztro.sameerkumar.website/?sign=cancer&day=today')
        assert endpoint == result
    
    @patch('requests.post')
    def test_if_request_is_done_to_api_endpoint(self, mock_post):
        
        mock_post.return_value = Mock(status_code=200, content= """{"content":{ "date_range": "Jun 22 - Jul 22",
                                                                    "current_date": "May 21, 2022",
                                                                    "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                                                    "compatibility": "Scorpio",
                                                                    "mood": "Pleasant",
                                                                    "color": "Orange",
                                                                    "lucky_number": "46",
                                                                    "lucky_time": "5pm"
                                                                }}""")
        extract_class = HoroscopeExtract()
        endpoint= (f'https://aztro.sameerkumar.website/?sign=cancer&day=today')
        result = extract_class.request_data_to_api(endpoint=endpoint)
        
        assert result == {"content":{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    }}
        mock_post.assert_called_with(endpoint)
        
    @mock.patch('horoscope_observatory.horoscope_extract.HoroscopeExtract.request_data_to_api')
    def test_if_extract_method_calls_other_methods(self, request_data):
        request_data.return_value = { "date_range": "Jun 22 - Jul 22",
                                                "current_date": "May 21, 2022",
                                                "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                                "compatibility": "Scorpio",
                                                "mood": "Pleasant",
                                                "color": "Orange",
                                                "lucky_number": "46",
                                                "lucky_time": "5pm"
                                            }
        extract_class = HoroscopeExtract()
        result = extract_class.extract()
        assert result == [{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },{ "date_range": "Jun 22 - Jul 22",
                                        "current_date": "May 21, 2022",
                                        "description": "Your ordinary routine will be far from ordinary, no matter how hard you try to make it so. Be prepared for anything and everything to happen -- and be ready to enjoy every single second of it.",
                                        "compatibility": "Scorpio",
                                        "mood": "Pleasant",
                                        "color": "Orange",
                                        "lucky_number": "46",
                                        "lucky_time": "5pm"
                                    },]