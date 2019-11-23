from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():\
    return 'Hello World!'


@app.route('/data')
def data():
    d = {'point1': [42, 10],
         'point2': [12, 17]}
    return jsonify(d)


if __name__ == '__main__':
    app.run()
