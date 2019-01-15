# import artm
from flask import Flask

app = Flask(__name__)

# start service ( python -m flask run )


@app.route('/', methods=['PUT'])
def hello_world():
    return 'Hello, World!'
