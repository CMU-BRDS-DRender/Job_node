from flask import jsonify
class StatusManager:
    def __init__(self, message_uri, jobId):
        self.message_uri = message_uri
        self.queue_name = 'StatusQueue'+ str(jobId)
        self.exchange = ''
        self.routing_key = 'StatusQueue'+ str(jobId)
        self.jobId = jobId

def send_status(self, no_of_frames):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.message_uri))
        channel = connection.channel()
        channel.queue_declare(queue = self.queue_name)
        body = {}
        body['jobId'] = self.jobId
        body['no_of_frames'] = self.no_of_frames
        channel.basic_publish(exchange=self.exchange, routing_key = self.routing_key, body = jsonify(body))
        print("[x] Sent 'Alive' ")
        connection.close()
