import os
import boto3
import botocore



s3 = boto3.resource('s3',
					aws_access_key_id = 'XXXXXXXXXXXXXXXXXXX',
					aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

s3.Bucket('renderframe').upload_file('home/Rendered/butterfly (1).jpg', 'renderedframe_0001')
