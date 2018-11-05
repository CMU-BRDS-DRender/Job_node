import boto3
import botocore
import os

class S3Driver:
	def __init__(self, input_bucket, input_file_path, output_bucket, output_file_path):
		self.input_bucket = input_bucket
		self.input_file_path = input_file_path
		self.output_bucket = output_bucket
		self.output_file_path = output_file_path
		self.s3_client = boto3.resource('s3', aws_access_key_id = os.environ['aws_access_key_id'], aws_secret_access_key = os.environ['aws_secret_access_key'])
		self.local_directory = 'drender'

	def download_file(self):
		if not os.path.exists(self.local_directory):
			os.makedirs(self.local_directory)
			self.s3_client.Bucket(self.input_bucket).download_file(self.input_file_path, self.local_directory + '/' + os.path.basename(self.input_file_path))

	def upload_file(self,file_name):
		file_path = self.local_directory+ "/"+ file_name
		if not os.path.exists(file_path):
			print(file_path)
			return
		print(file_path)
		print(self.output_file_path)
		self.s3_client.Bucket(self.output_bucket).upload_file(file_path,self.output_file_path+file_name)
