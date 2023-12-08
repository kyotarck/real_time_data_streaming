from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic

def build_producer():
    try :
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('mon_topic', b'Message Test')
    except KafkaError as e:
        print(f"Erreur Kafka: {e}")

build_producer()