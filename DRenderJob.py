import subprocess
import os
import threading
from time import sleep
from S3Driver import S3Driver
from StatusManager import StatusManager
class DRenderJob:

	def __init__(self, jobid, start_frame, end_frame, input_bucket, input_file_path, output_bucket, output_file_path, project_ID, message_uri,message_queuename):
		self.jobid = jobid
		self.start_frame = start_frame
		self.end_frame = end_frame
		self.frames_rendered = []
		self.last_frame_rendered = 0
		self.project_ID = project_ID
		self.status = "RUNNING"
		self.jobStatusQueue = StatusManager(message_uri, jobid,message_queuename)
		self.s3Driver = S3Driver(input_bucket, input_file_path, output_bucket, output_file_path)
		self.s3Driver.download_file()

	def start(self):
		t1 = threading.Thread(target=self.render)
		t1.start()



	def render(self):
		for i in range(self.start_frame, self.end_frame +1) :
			self.render_frame(i)
		self.status = "COMPLETED"


	def render_frame(self, frame_number):
		input_file_path = self.s3Driver.local_directory + "/" + os.path.basename(self.s3Driver.input_file_path)
		output_file_path = self.s3Driver.local_directory + "/frame-#.jpg"
		command = "blender -b " + input_file_path + " -o " + output_file_path + " -F JPEG -f "+ str(frame_number)
		output = subprocess.call(command,shell=True)
		self.s3Driver.upload_file("frame-"+str(frame_number)+".jpg");

		#sleep(20)
		# push jobid and frame_number om Rabbit mQ
		self.frames_rendered.append(frame_number);
		self.last_frame_rendered = frame_number
		try:
			self.jobStatusQueue.send_status(self.frames_rendered, self.last_frame_rendered, self.s3Driver.output_file_path + "frame-"+str(frame_number)+".jpg", self.s3Driver.output_bucket)
		except Exception as e:
			print(e)
