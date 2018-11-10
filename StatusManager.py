import json
import pika


class StatusManager:
    def __init__(self, message_uri, jobId,message_queuename):
        self.message_uri = message_uri
        self.queue_name = message_queuename
        self.exchange = ''
        self.routing_key = message_queuename
        self.jobId = jobId

    def send_status(self, no_of_frames, frames_rendered, file_path, bucket_name):
            credentials = pika.PlainCredentials(username="drender", password="brds")
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.message_uri, credentials=credentials))
            channel = connection.channel()
            #channel.queue_declare(queue = self.queue_name)
            body = {}
            body['jobId'] = self.jobId
            body['no_of_frames'] = no_of_frames
            body['lastFrameRendered'] = frames_rendered
            outputURI = {}
            outputURI['bucketName'] = bucket_name
            outputURI['file'] = file_path
            body['outputURI'] = outputURI
            channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=json.dumps(body))
            print("[x] Sent 'Alive' ")
            connection.close()
