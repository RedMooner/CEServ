from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    command = request.args.get('command')

    if command:
        try:
            result = subprocess.check_output(command, shell=True)
            print(result)
            return result
        except Exception as e:
            return str(e)
    
    return 'No command provided.'

if __name__ == '__main__':
    app.run(port="5001",host="127.0.0.1",debug=True)