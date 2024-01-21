from faker import faker
from models import Contact
import connect_mongo
import connect_rmq as rmq

message = "Hey there and here!"
queue_name = "sms"

def generate_contacts(num_contacts):
    ...

def save_to_db(contacts):
    Contact(**contacts).save()

def put_to_queue(user_id):
    rmq.channel.queue_declare(queue=queue_name)
    rmq.channel.basic_publish(exchange='', routing_key=queue_name, body=user_id.encode())


def main():
    contacts = generate_contacts(10)
    save_to_db(contacts)
    for contact in contacts:
        db_contact = Contact.object(contact__fullname=contact.name) # ? check with faker
        put_to_queue(db_contact.id) 
        db_contact.update(sent=True)

if __name__ == "__main__":
    main()
    # rmq connection opens in connect_rmq module, need to close
    rmq.connection.close()