from flask import Flask
app = Flask(__name__)

@app.route('/start', methods=['POST'])
def status_to_master():
    return 'Frame sent for rendering'
