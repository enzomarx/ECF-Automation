from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def show_log():
    log_file = 'automacao.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            log_content = file.read()
    else:
        log_content = "Log file not found."
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Log de Automação</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .log-container {
                margin: 20px;
                padding: 10px;
                border: 1px solid #ccc;
                background-color: #f9f9f9;
                max-height: 500px;
                overflow-y: auto;
            }
        </style>
    </head>
    <body>
        <h1>Log de Automação</h1>
        <div class="log-container" id="log-container">
            <pre id="log-content">{{ log_content }}</pre>
        </div>
        <script src="https://cdn.socket.io/4.0.1/socket.io.min.js"></script>
        <script>
            var socket = io();
            socket.on('log_update', function(data) {
                var logContainer = document.getElementById('log-container');
                var logContent = document.getElementById('log-content');
                logContent.textContent += data.message + '\\n';
                logContainer.scrollTop = logContainer.scrollHeight;
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template, log_content=log_content)

@socketio.on('log_update')
def handle_log_update(data):
    emit('log_update', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
