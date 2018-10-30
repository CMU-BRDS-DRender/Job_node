from flask import Flask, jsonify, request
import os
import boto3
import botocore
app = Flask(__name__)

@app.route('/start', methods=['POST'])
def testPost():
	if request.method == 'POST':
		ID = request.json['ID']
		project_ID = request.json['projectID']
		source_url = request.json['source']
		start_frame = request.json['startFrame']
		end_frame = request.json['endFrame']
		action = request.json['action']
		bucket_url = request.json['outputURI']
		
os.system("blender -b /XXXXXXXX/scene-Helicopter-27.blend -o /XXXXXXX -f 'start_frame' -a")

#os.system("blender -b /mnt/c/Users/Mihir/Downloads/Demo_274/scene-Helicopter-27.blend -o /mnt/c/Users/Mihir/Downloads/Demo_274/Rendered -f 1 -a")
