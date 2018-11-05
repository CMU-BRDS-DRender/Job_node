import subprocess
import os
import threading
from time import sleep
from S3Driver import S3Driver

class DRenderJob:

	def __init__(self, jobid, start_frame, end_frame, input_bucket, input_file_path, output_bucket, output_file_path, project_ID):
		self.jobid = jobid
		self.start_frame = start_frame
		self.end_frame = end_frame
		self.no_of_frames_rendered = -1
		self.project_ID = project_ID
		self.status = "RUNNING"
		self.s3Driver = S3Driver(input_bucket, input_file_path, output_bucket, output_file_path)
		self.s3Driver.download_file()
		print(self.start_frame)

	def start(self):
		print(self.start_frame)
		t1 = threading.Thread(target=self.render)
		t1.start()



	def render(self):
		for i in range(self.start_frame, self.end_frame +1) :
			print(i)
			self.render_frame(i)
		self.status = "COMPLETED"


	def render_frame(self, frame_number):
		input_file_path = self.s3Driver.local_directory + "/" + os.path.basename(self.s3Driver.input_file_path)
		output_file_path = self.s3Driver.local_directory + "/frame-"+str(frame_number)
		command = "blender -b "+ input_file_path + " -o " + output_file_path+" -f "+ str(frame_number) +" -a"
		output = subprocess.call(command,shell=True)
		sleep(10)
		print(frame_number)
		self.s3Driver.upload_file('frame-'+str(frame_number));
		# push jobid and frame_number om Rabbit mQ
		self.no_of_frames_rendered = frame_number;
