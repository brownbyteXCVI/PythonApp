from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Code still works just by activating the venv '