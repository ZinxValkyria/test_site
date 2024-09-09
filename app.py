from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Define the S3 URL from environment variables
S3_BASE_URL = os.getenv("S3_BASE_URL")

# Base template for the workflow
BASE_TEMPLATE = '''
name: Generated Workflow

on:
  push: {{ push_trigger }}
  pull_request: {{ pull_request_trigger }}

jobs:
  main_job:
    runs-on: {{ os }}
    steps:
{{ checkout_step }}
{{ predefined_actions }}
{{ custom_steps }}
'''

# Load YAML scripts from S3
def load_script(script_name):
    script_url = f"{S3_BASE_URL}/{script_name}.yml"
    response = requests.get(script_url)
    if response.status_code == 200:
        return response.text
    else:
        return ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_yaml():
    task = request.form.get('task')
    os_type = request.form.get('os')
    additional_actions = request.form.getlist('additional_actions')
    direct_commands = request.form.get('direct_commands')

    # Load base and checkout scripts
    base_script = load_script('base')
    checkout_script = load_script('checkout')

    # Load predefined actions based on the main task
    predefined_actions = load_script(task)

    # Handle additional actions
    additional_actions_str = ''
    for action in additional_actions:
        additional_actions_str += load_script(action) + '\n'

    # Handle direct commands
    if direct_commands:
        custom_steps = "- name: Run Direct Commands\n  run: |\n    {}\n".format(
            direct_commands.replace('\n', '\n    ')
        )
    else:
        custom_steps = ''

    # Populate the base template
    script = BASE_TEMPLATE
    script = script.replace('{{ os }}', os_type)
    script = script.replace('{{ checkout_step }}', checkout_script)
    script = script.replace('{{ predefined_actions }}', predefined_actions)
    script = script.replace('{{ custom_steps }}', additional_actions_str + custom_steps)
    
    # Handle triggers
    push_trigger = 'true' if 'push' in request.form.getlist('triggers') else 'false'
    pull_request_trigger = 'true' if 'pull_request' in request.form.getlist('triggers') else 'false'
    script = script.replace('{{ push_trigger }}', push_trigger)
    script = script.replace('{{ pull_request_trigger }}', pull_request_trigger)

    return jsonify({'yaml': script})

if __name__ == '__main__':
    app.run(debug=True)
