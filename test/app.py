import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/run_script')
def run_script():
    result = subprocess.run(['python', '/templates/server.py' ], capture_output=True, text=True)
    return result.stdout


if __name__ == '__main__':
    app.run()
    