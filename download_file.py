import os
import boto3
import botocore

directory = '/home/Blender'
if not os.path.exists(directory):
    os.makedirs(directory)




s3 = boto3.resource('s3',
					aws_access_key_id = 'XXXXXXXXXXXXXXXXXXX',
					aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

s3.Bucket('renderframe').download_file('butterfly (1).jpg', '/home/Blender/to_be_rendered_frame_0001')
