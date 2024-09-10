import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Define the directory where YAML scripts are stored
SCRIPTS_DIR = os.path.join(os.getcwd(), 'scripts')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_yaml/<task>.yaml', methods=['GET'])
def fetch_yaml(task):
    yaml_file = f"{task}.yaml"
    # Check if the file exists before trying to send it
    if os.path.isfile(os.path.join(SCRIPTS_DIR, yaml_file)):
        return send_from_directory(SCRIPTS_DIR, yaml_file)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
