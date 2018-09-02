from kafka import KafkaConsumer
from kafka import KafkaProducer
consumer = KafkaConsumer('validate_phone',bootstrap_servers=['localhost:9092'])
producer = KafkaProducer(bootstrap_servers='localhost:9092')

print "OPS listening..."
for message in consumer:
	print ("key=%s value=%s" % (message.key, message.value))
	if message.key == "number":
		producer.send('validate_phone_result', b'Validated',key="result")
	

