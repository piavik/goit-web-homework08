import json, random
from faker import Faker
from models import Contact
import connect_mongo
import connect_rmq as rmq


message = "Hey there and here!"
# queue_name = "sms"

def generate_contacts(num_contacts: int) -> list:
    fake = Faker()
    contacts = []
    for _ in range(num_contacts):
        record = fake.json(data_columns={
            "name": "name", 
            "address": "address", 
            "phones": [{"number": "phone_number"}, {"number": "phone_number"}],
            "email": "safe_email", 
            "tags": [{"name": "word"}, {"name": "word"}, {"name": "word"}],
            }, num_rows=1)
        contact = json.loads(record)
        contact["pref_method"] = random.choice(["sms", "email"])
        contacts.append(contact)
    return contacts

def save_to_db(contacts: list):
    Contact.drop_collection()
    for contact in contacts:
        Contact(**contact).save()

def put_to_queue(user_id, queue_name):
    rmq.channel.queue_declare(queue=queue_name)
    rmq.channel.basic_publish(exchange='', routing_key=queue_name, body=user_id)

def main():
    contacts = generate_contacts(10)
    save_to_db(contacts)
    db_contacts = Contact.objects()
    for contact in db_contacts:
        preferred_method = contact.pref_method
        put_to_queue(str(contact.id).encode(), preferred_method) 

if __name__ == "__main__":
    main()
    # rmq connection opens in connect_rmq module, need to close
    rmq.connection.close()
