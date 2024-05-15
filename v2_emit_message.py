"""

Message sender / emitter 

Description:
This script sends one message on a named queue.
It will execute and finish. 
You can change the message and run it again in the same terminal.

Remember:
- Use the up arrow to recall the last command executed in the terminal.
"""

# Import from Standard Library
import sys

# Import External packages used
import pika

# Configure logging
from util_logger import setup_logger

logger, logname = setup_logger(__file__)

# ---------------------------------------------------------------------------
# Define program functions (bits of reusable code)
# ---------------------------------------------------------------------------


def send_message(host: str, queue_name: str, message: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue

    """

    try:
        # create a blocking connection to the RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        # use the connection to create a communication channel
        ch = connection.channel()

        # use the channel to declare a queue
        ch.queue_declare(queue="v2_task")

        # use the channel to publish a message to the queue
        ch.basic_publish(exchange="", routing_key="v2_task", body="Oh hey, it works! We did it... where's my cup of coffee??")

        # log a message for the user
        logger.info(f" [x] Sent {message}")
        print(f" [x] sent {message}")

    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        connection.close()


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    send_message("localhost", "v2_task", "Oh hey, it works! We did it... where's my cup of coffee??")
