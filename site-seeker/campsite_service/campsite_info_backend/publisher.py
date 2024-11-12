import pika
import json


def send_booking_message(booking_data):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='booking_queue')

    channel.basic_publish(
        exchange='',
        routing_key='booking_queue',
        body=json.dumps(booking_data))

    connection.close()
