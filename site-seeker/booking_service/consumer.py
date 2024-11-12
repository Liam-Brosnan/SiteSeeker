import os
import pika
import json
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_service.settings')
django.setup()

from booking_app.models import Booking


def create_booking(ch, method, properties, body):
    data = json.loads(body)
    booking = Booking.objects.create(
        booking_id=data['booking_id'],
        campsite_id=data['campsite_id'],
        check_in_date=data['check_in_date'],
        check_out_date=data['check_out_date'],
        number_of_people=data['number_of_people'],
    )
    print(f"Booking created. Booking ID: {booking.booking_id}")


def start_consuming():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost',))
    channel = connection.channel()
    channel.queue_declare(queue='booking_queue')

    channel.basic_consume(queue='booking_queue',
                          on_message_callback=create_booking, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    start_consuming()
