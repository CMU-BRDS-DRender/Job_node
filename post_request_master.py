from flask import Flask, jsonify, request, response
app = Flask(__name__)

jobs_executed = {}

@app.route('/start', methods=['GET', 'POST'])
def start():
	if (request.method == 'POST'):
		jobId = request.json['ID']
		project_ID = request.json['projectID']
		source_url = request.json['source']
		start_frame = request.json['startFrame']
		end_frame = request.json['endFrame']
		action = request.json['action']
		bucket_url = request.json['outputURI']
		current_job = DRenderJob(start_frame, end_frame, input_bucket, input_file_path, output_bucket, output_file_path. project_ID)
		jobs_executed[jobId] = current_job
		current_job.start()
		response = {}

		response['content-type'] = 'application/json'
		response['status-code'] = 200
		response['message'] = 'Bhak bsdk'

		return jsonify(response)

@app.route('/status/<jobId>', methods=['GET'])
def status(jobId):
	job = None
	response = {}
	response['content-type'] = 'application/json'


	if jobId in jobs_executed :
		job = jobs_executed[jobId]
		response['status-code'] = 200
		response['body'] = {
			jobStatus : job.status
			framesRendered : job.no_of_frames_rendered
			jobId : jobId
			message: 'Job ' + jobId + ' is in progress'
		}
	else:
		response['status-code'] = 400
		response['body'] = {
			message: 'Job ' + jobId + ' does not exist'
			jobId : jobId
		}
	return jsonify(response)





if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 8080, debug = True )
