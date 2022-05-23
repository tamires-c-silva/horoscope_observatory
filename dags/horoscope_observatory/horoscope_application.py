
import logging
from yaml import load
from horoscope_observatory.horoscope_load import HoroscopeLoad
from horoscope_observatory.horoscope_extract import HoroscopeExtract
from horoscope_observatory.horoscope_transform import HoroscopeTransform




class HoroscopeApplication:
    
    def process(self):
        extracted_data = HoroscopeExtract().extract()
        if extracted_data:
            transformed_data = HoroscopeTransform().transform(extracted_data=extracted_data)
            HoroscopeLoad().load(transformed_data=transformed_data)
            return