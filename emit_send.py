# See Hello World! Example at
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# Note: Make sure that RabbitMQ is started and running. While it may perform processes in the background it must be turned on for this to work.

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")
connection.close()
