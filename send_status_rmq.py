# tested only for sending single message on Win


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key = 'hello',
                      body = 'Alive')
print("[x] Sent 'Alive' ")
connection.close()