from flask import Flask, jsonify, request
from DRenderJob import DRenderJob
app = Flask(__name__)

jobs_executed = {}

@app.route('/start', methods=['POST'])
def start():
    jobId = request.json['ID']
    project_ID = request.json['projectID']
    source_URI = request.json['source']
    input_bucket = source_URI['bucketName']
    input_file_path = source_URI['file']
    start_frame = request.json['startFrame']
    end_frame = request.json['endFrame']
    destination_URI = request.json['outputURI']
    output_bucket = destination_URI['bucketName']
    output_file_path = destination_URI['file']
    new_job = DRenderJob(jobId, start_frame, end_frame, input_bucket, input_file_path, output_bucket, output_file_path, project_ID)
    jobs_executed[jobId] = new_job
    new_job.start()
    response = {}
    response['status-code'] = 200
    response['message'] = 'Job ' + str(jobId) + ' has started'
    return jsonify(response)

@app.route('/status/<jobId>', methods=['GET'])
def status(jobId):
    if jobId is None:
        response = {}
        response['status-code'] = 200
        response['body'] = {}
        response['body']['message'] = 'Service running'
        return jsonify(response)
        
    job = None
    response = {}
    if jobId in jobs_executed:
        job = jobs_executed[jobId]
        print(job.status)
        response['status-code'] = 200
        response['body'] = {}
        response['body']['jobStatus'] = job.status
        response['body']['framesRendered'] = job.no_of_frames_rendered
        response['body']['jobId'] = jobId
        response['body']['message'] = 'Job ' + jobId + ' is in progress'
        return jsonify(response)

	response['status-code'] = 400
    response['body'] = {}
    response['body']['message'] = 'Job ' + jobId + ' does not exist'
    response['body']['jobId'] = jobId
    return jsonify(response)

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 8080, debug = True )
