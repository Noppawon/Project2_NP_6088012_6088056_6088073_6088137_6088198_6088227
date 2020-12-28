from kafka import KafkaConsumer
from json import loads
from time import sleep
import json
from multiprocessing import Process
import binascii


consumer = KafkaConsumer(
    'VanHubBusTerminal-topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)


for event in consumer:
    event_data = event.value
    # Do whatever you want
    print("Consumer records:")
    print(event_data)
    print("Ticket office:", event[6]['from_name'])
    print("Van Station id:", event[6]['station_number'])
    print("Van Color:", event[6]['van_color'])
    print("Destionation:", event[6]['to_name'])
    print("=========\n")

    sleep(2)


# consumer = KafkaConsumer('topic_building_A',bootstrap_servers = ['localhost:9092'],
#         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# consumer_building_A = KafkaConsumer('topic_building_A',bootstrap_servers = ['localhost:9092'],
#         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
#
#
# consumer_building_B = KafkaConsumer('topic_building_B',bootstrap_servers = ['localhost:9092'],
#         value_deserializer=lambda m: json.loads(m.decode('utf-8')))






