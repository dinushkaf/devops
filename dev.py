from kafka import KafkaProducer
from kafka import KafkaConsumer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer('validate_phone_result',bootstrap_servers=['localhost:9092'])

#send phone number
producer.send('validate_phone', b'0711234567',key="number")
for msg in consumer:
	if msg.key == "result":
		print msg.value
		break
