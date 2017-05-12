from flask import Flask
app = Flask(__name__)

@app.route('/api/index')
def api_index():
    return '{"status":"all good"}'
