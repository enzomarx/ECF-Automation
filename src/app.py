from flask import Flask, render_template_string
import os

app = Flask(__name__)

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
        <div class="log-container">
            <pre>{{ log_content }}</pre>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, log_content=log_content)

if __name__ == "__main__":
    app.run(debug=True)
