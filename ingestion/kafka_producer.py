from kafka import KafkaProducer
import json
import pandas as pd

# Load shipment data
data = pd.read_csv('../data/shipment_data.csv')

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send data to Kafka topic
for _, row in data.iterrows():
    producer.send('logistics_topic', row.to_dict())

producer.flush()
print("Streaming Completed")
