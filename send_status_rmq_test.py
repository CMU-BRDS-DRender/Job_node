=# tested only for sending single message on Win

class StatusMessages:
	def __init__(self, masterIP, queue_name, exchange, routing_key, jobId, frame_number):
		self.masterIP = 'localhost'
		self.queue_name = 'StatusQueue'
		self.exchange = ''
		self.routing_key = 'StatusQueue'
		self.jobId = 10
		self.frame_number = 5

	def send_status(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters(self.masterIP))
		channel = connection.channel()
		channel.queue_declare(queue = self.queue_name)
		channel.basic_publish(exchange=self.exchange, routing_key = self.routing_key, body = str(self.jobId) + str(self.frame_number))
		print("[x] Sent 'Alive' ")
		connection.close()
