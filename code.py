from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! Welcome to my Python app running in Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
