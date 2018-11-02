from flask import Flask
app = Flask(__name__)

@app.route('/start', methods=['POST'])
def status_to_master():
    return 'Frame sent for rendering'

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 8080, debug = True)
