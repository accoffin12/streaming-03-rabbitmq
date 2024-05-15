"""
    This program sends a message to a queue on the RabbitMQ server.
    Be sure that the RabbitMQ service is on and connected. 
    Run this first, then run v1_listern_for_messages.py.
"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue="hello")

# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body="We've got this")

# print a message to the console for the user
print(" [x] Sent 'Hello World!'")

# close the connection to the server
conn.close()
