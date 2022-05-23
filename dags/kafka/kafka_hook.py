import json
import logging
from multiprocessing import process
import shlex
import subprocess
from time import sleep
from json import dumps
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


class KafkaHook:

    def process_kafka(self, data_to_load):
        
        self.send_data_to_kafka(data_to_load=data_to_load)
        
        logging.info("Data sent to Kafka")
        return 
    
    def send_data_to_kafka(self, data_to_load):
        
        value_schema = avro.load('dags/kafka/ValueSchema.avsc')
        key_schema = avro.load('dags/kafka/KeySchema.avsc')
        key = {"name": "horoscope_observatory"}
        
        data_to_load_dict = data_to_load.to_dict('records')
        avroProducer = AvroProducer(
            {'bootstrap.servers': 'broker:29092', 'schema.registry.url': 'http://schema-registry:8081',
             'log_level':7, 'debug':'all'},
            default_key_schema=key_schema, default_value_schema=value_schema)
        
        for data_to_load_item in data_to_load_dict:
            avroProducer.produce(topic='horoscope_topic', value=data_to_load_item, key=key, key_schema=key_schema, value_schema=value_schema)
            
        
        avroProducer.flush(10)
        return

    