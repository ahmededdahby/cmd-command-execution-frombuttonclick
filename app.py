from flask import Flask, render_template
from flask import request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_dir', methods=['POST'])
def execute_dir():
    your_command = "dir"
    result = subprocess.run(your_command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout
        output_lines = output.splitlines()
        return render_template('output.html', output_lines=output_lines)
    else:
        error = result.stderr
        return render_template('error.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)