import subprocess
import os
import threading
from time import sleep
from S3Driver import S3Driver
from StatusManager import StatusManager
class DRenderJob:

	def __init__(self, jobid, start_frame, end_frame, input_bucket, input_file_path, output_bucket, output_file_path, project_ID, message_uri):
		self.jobid = jobid
		self.start_frame = start_frame
		self.end_frame = end_frame
		self.frames_rendered = []
		self.project_ID = project_ID
		self.status = "RUNNING"
		self.jobStatusQueue = StatusManager(message_uri, jobId)
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
		output_file_path = self.s3Driver.local_directory + "/frame-"+str(frame_number)
		command = "blender -b "+ input_file_path + " -o " + output_file_path+" -f "+ str(frame_number) +" -a"
		output = subprocess.call(command,shell=True)
		sleep(10)
		self.s3Driver.upload_file('frame-'+str(frame_number));
		# push jobid and frame_number om Rabbit mQ
		self.frames_rendered.append(frame_number);
		self.jobStatusQueue.send_status(self.frames_rendered)
