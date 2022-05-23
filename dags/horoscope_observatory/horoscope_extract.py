import json
import logging
from pickletools import read_uint1
import re
import requests

class HoroscopeExtract:
    
    signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
    day = 'today'
    
    def extract(self):
        list_of_extracted_data = list()
        for sign in self.signs:
            list_of_extracted_data.append(self.request_data_to_api(endpoint=self.format_api_endpoint(sign=sign, day=self.day)))
        return list_of_extracted_data
    
    def format_api_endpoint(self,sign, day):
        endpoint = (f'https://aztro.sameerkumar.website/?sign={sign}&day={day}')
        return endpoint
    
    def request_data_to_api(self, endpoint):
        request_answer = requests.post(endpoint)
        request_content = json.loads(request_answer.content)
        
        return request_content
    