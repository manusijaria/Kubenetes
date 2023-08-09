import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(message="Welcome to My Flask App! Send a POST request to /run_pipeline to run the pipeline.") 

@app.route('/run_code', methods=['POST'])
def home():
    import subprocess
    output = subprocess.check_output(["docker", "run", "src-my_python_app"])
    return f"<pre>{output.decode('utf-8')}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)