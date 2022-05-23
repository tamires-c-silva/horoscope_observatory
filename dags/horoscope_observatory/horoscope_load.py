from kafka.kafka_hook import KafkaHook


class HoroscopeLoad:
    def load(self, transformed_data):
        KafkaHook().process_kafka(transformed_data)
        return
    