# CEServ
Command Executor server
# The server executing the commands
## Description of the CommandExecutor Server

CommandExecutor Server (Server) is a server application capable of accepting commands via GET requests and executing them for the user. After executing the command, the server returns the appropriate response.

#### Features:
- Accepts commands in the format of GET requests
- Executes commands on a physical server
- Sends responses after completing the command execution
- Can be customized for various tasks and functionality

#### Usage example:
1. Send a GET request to the server with the command to be executed
2. The server will execute the command on the physical server
3. After completion of the execution, the server will send a response with the result of the command

CEServ provides a convenient and flexible system for executing commands and receiving responses, which makes it a universal tool for automating and managing tasks on the server.


# Introduction

It happens that there is a need to execute a command on the server and send its result somewhere else.

To solve such a problem, a simple solution was implemented, which will be shown below.

## Zabbix

There is a Zabbix server, and it is possible to execute JavaScript code on network nodes. Our task was to get the exhaust of a certain command on the server and send the result to the Zabbix client for subsequent processing.

# Solving the problem

Let's write a simple server on flask that will process requests and execute commands on a physical server.

```python
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
```

In order to interact with the server using the java script language, you can use the following code:

```jsx
var request = new HttpRequest();
return request.get("command_text", (value));
```

The result will be the execution of the command on the server and the transfer of the result of the command execution to the client.

# TODO

- Implement black and white lists of commands to ensure security;
- Implement the server installer and configurator.
