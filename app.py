from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    d = {'point1': [42, 10],
         'point2': [12, 17]}
    return jsonify(d)


if __name__ == '__main__':
    app.run()
