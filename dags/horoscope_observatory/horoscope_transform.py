import logging
from nrclex import NRCLex
import json
import pandas as pd

class HoroscopeTransform:
    
    def transform(self, extracted_data):
        horoscope_dataframe = self.create_dataframe_using_extracted_data(extracted_data=extracted_data)
        transformed_data = self.analyse_feeling(horoscope_dataframe=horoscope_dataframe)

        return transformed_data
    
    
    def create_dataframe_using_extracted_data(self, extracted_data):
        horoscope_dataframe = pd.DataFrame(extracted_data)
        return horoscope_dataframe
    
    def convert_dict_to_list_of_dict(self, row, key_name, value_name):
        return [{f'{key_name}':k, f'{value_name}':v} for k,v in row.items()]
    
    def analyse_feeling(self, horoscope_dataframe):
        horoscope_dataframe['feeling_analysis_affect_dict'] = horoscope_dataframe.apply(lambda row: NRCLex(row.description).affect_dict, axis =1)
        
        horoscope_dataframe['feeling_analysis_affect_dict'] = horoscope_dataframe.apply(lambda row: 
            self.convert_dict_to_list_of_dict(row =row.feeling_analysis_affect_dict, key_name="word", value_name="feelings"), axis=1)
        
        return horoscope_dataframe