import os
import threading

class DRenderJob:

	def __init__(self, jobid, start_frame, end_frame, input_bucket, input_file_path, output_bucket, output_file_path, project_ID):
		self.jobid = jobid
		self.start_frame = start_frame
		self.end_frame = end_frame
		self.no_of_frames_rendered = -1
		self.project_ID = project_ID
		self.s3Driver = S3Driver(input_bucket, input_file_path, output_bucket, output_file_path)

	def start(self):
		t1 = threading.Thread(target=render)


	def render(self):
		for i in range [self.start_frame, self.end_frame +1] :
			render_frame(i)

	def render_frame(self, frame_number):
		os.system("blender -b /home/ubuntu/Blender/"+ os.path.basename(self.s3Driver.output_file_path) + " -o /home/ubuntu/Blender/Rendered/frame-"+str(frame_number)+" -f "+ str(frame_number) +" -a")
		self.s3Driver.upload_file('Rendered/frame-'+str(frame_number));
		# push jobid and frame_number om Rabbit mQ		
		self.no_of_frames_rendered = frame_number;

