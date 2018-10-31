from flask import Flask, jsonify, request
import os
import boto3
import botocore
app = Flask(__name__)
directory = '/home/Blender/Rendered'

@app.route('/start', methods=['POST'])
def testPost():
	if (request.method == 'POST'):
		ID = request.json['ID']
		project_ID = request.json['projectID']
		source_url = request.json['source']
		start_frame = request.json['startFrame']
		end_frame = request.json['endFrame']
		action = request.json['action']
		bucket_url = request.json['outputURI']
		return jsonify(start_frame)
		if not os.path.exists(directory):
    			os.makedirs(directory)
			
	if (request.method == 'GET'):
		return "Status: 200 OK!"
if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 8080, debug = True)
		
		
		os.system("blender -b /home/Blender/to_be_rendered.blend -o /home/Blender/Rendered/rendered_001 -f 1 -a")
		


#os.system("blender -b /mnt/c/Users/Mihir/Downloads/Demo_274/scene-Helicopter-27.blend -o /mnt/c/Users/Mihir/Downloads/Demo_274/Rendered -f 1 -a")
