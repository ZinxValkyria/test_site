import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templatesv2')

# Define the directory where local YAML scripts are stored
SCRIPTS_DIR = os.path.join(os.getcwd(), 'scripts')

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')  # Optional homepage

# Route for AWS page
@app.route('/aws')
def aws():
    return render_template('aws.html')

@app.route('/github')
def github():
    return render_template('github.html')

# Route for GCP page
@app.route('/gcp')
def gcp():
    return render_template('gcp.html')

# Route for Docker page
@app.route('/docker')
def docker():
    return render_template('docker.html')

# Route for Azure page
@app.route('/azure')
def azure():
    return render_template('azure.html')

# Route for GitHub Pages
@app.route('/custom')
def gh_pages():
    return render_template('custom.html')

# Route to fetch YAML files from local storage
@app.route('/fetch_yaml/<task>.yaml', methods=['GET'])
def fetch_yaml(task):
    yaml_file = f"{task}.yaml"
    file_path = os.path.join(SCRIPTS_DIR, yaml_file)
    
    # Check if the file exists before trying to send it
    if os.path.isfile(file_path):
        return send_from_directory(SCRIPTS_DIR, yaml_file)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)


# Load environment variables from .env file
# load_dotenv('my.env')

# app = Flask(__name__)

# # # Get the S3 base URL from environment variable
# S3_BASE_URL = os.getenv('S3_BASE_URL')

# @app.route('/fetch_yaml/<task>.yaml', methods=['GET'])
# def fetch_yaml(task):
#     yaml_file = f"{task}.yaml"
#     file_url = f"{S3_BASE_URL}/{yaml_file}"

#     try:
#         # Send an HTTP GET request to fetch the file from S3 public URL
#         response = requests.get(file_url)

#         # Check if the file exists
#         if response.status_code == 200:
#             # Return the file content as a response
#             return Response(response.content, mimetype='application/x-yaml')
#         else:
#             return "File not found", 404

#     except Exception as e:
#         return f"An error occurred: {str(e)}", 500

# if __name__ == '__main__':
#     app.run(debug=True)
