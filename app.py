
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Python App</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 100px;
                background: #f0f4f8;
            }
            h1 { color: #2563eb; }
            button {
                padding: 12px 24px;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Hello from Python App!</h1>
        <p>My Python application is running in the browser....</p>
        <button onclick="alert('Your Python web app is working!')">
            Click Me
        </button>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
