import sys
from models import Contact
import connect_mongo
import connect_rmq as rmq


queue_name = "email"

def callback(ch, method, properties, body):
    user_id = body.decode()
    db_contact = Contact.objects(id=user_id).first()
    print(f'Message sent to user_id {user_id} via email {db_contact.email}')
    db_contact.update(sent=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    rmq.channel.queue_declare(queue=queue_name)
    rmq.channel.basic_qos(prefetch_count=1)
    rmq.channel.basic_consume(queue=queue_name, on_message_callback=callback)
    rmq.channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
