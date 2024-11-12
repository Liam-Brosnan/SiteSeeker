import pika
import json


def publish_booking(booking_details):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
        ))
    channel = connection.channel()
    channel.queue_declare(queue='booking_queue', durable=True)

    message = {
        'campsite_id': booking_details.campsite_id,
        'start_date': booking_details.start_date.strftime('%Y-%m-%d'),
        'end_date': booking_details.strftime('%Y-%m-%d'),
        'number_of_people': booking_details.number_of_people
    }

    channel.basic_publish(
        exchange='',
        routing_key='booking_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,
        )
    )
    connection.close()
