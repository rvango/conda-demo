from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Flask!'

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run()
