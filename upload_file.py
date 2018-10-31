import os
import boto3
import botocore



s3 = boto3.resource('s3',
					aws_access_key_id = 'XXXXXXXXXXXXXXXXXXX',
					aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

s3.Bucket('renderframe').upload_file('/home/Blender/Rendered/rendered_001', 'renderedframe_0001')
