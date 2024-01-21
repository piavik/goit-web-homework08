import pika
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

# ----- RMQ -----
rmq_user = config.get('RMQ', 'user')
rmq_pass = config.get('RMQ', 'password')
rmq_host = config.get('RMQ', 'host')
rmq_port = config.get('RMQ', 'port')

# ----- connect -----
credentials = pika.PlainCredentials(rmq_user, rmq_pass)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmq_host, port=rmq_port, credentials=credentials))
channel = connection.channel()