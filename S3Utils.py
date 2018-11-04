import boto3
import botocore

class S3Driver:
	def __init__(self, input_bucket, input_file_path, output_bucket, output_file_path):
		self.input_bucket = input_bucket
		self.input_file_path = input_file_path
		self.output_bucket = output_bucket
		self.output_file_path = output_file_path
		self.s3_client = boto3.resource('s3',
				aws_access_key_id = 'XXXXXXXXXXXXXXXXXXX',
					aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
		self.local_directory = '/home/ubuntu/Blender' 

	def download_file(self):
		if not os.path.exists(self.local_directory):
    		os.makedirs(self.local_directory)
	 	s3.Bucket(self.input_bucket).download_file(self.input_file_path, self.local_directory + '/' + os.path.basename(self.input_file_path))		

	def upload_file(self,file_name):
		if not os.path.exists(file_path):
			# Throw Error
    		return
    	s3.Bucket(self.output_bucket).upload_file(self.local_directory+ "/"+ file_name, self.output_file_path)		
