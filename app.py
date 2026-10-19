import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <html>
        <head><title>Docker Demonstration</title></head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h2>🐳 Docker Container Demonstration App</h2>
            <form action="/greet" method="POST" style="margin-top: 20px;">
                Enter your name: <input type="text" name="username" required style="padding: 8px;">
                <input type="submit" value="Submit" style="padding: 8px 16px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">
            </form>
        </body>
        </html>
    '''


@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form.get('username', 'Guest')
    return f"""
        <html>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h2>🎉 Hello {user_input}!</h2>
            <p>Welcome to this app running inside a live Docker container.</p>
            <p><a href="/">← Back</a></p>
        </body>
        </html>
    """


@app.get('/health')
def health():
    return {"status": "healthy"}, 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port)