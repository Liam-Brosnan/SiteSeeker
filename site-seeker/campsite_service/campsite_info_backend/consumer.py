import pika
import json
from django.core.cache import cache


def callback(ch, method, properties, body):
    response = json.loads(body)

    cache.set(f'booking_response_{
              response["booking_id"]}', response, timeout=60*5)
    print("Received response and saved to cache:", response)

    ch.basic_ack(delivery_tag=method.delivery_tag)


# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the response queue
channel.queue_declare(queue='response_queue')

# Set up the consumer
channel.basic_consume(queue='response_queue', on_message_callback=callback)

print("Waiting for responses. To exit press CTRL+C")
channel.start_consuming()
