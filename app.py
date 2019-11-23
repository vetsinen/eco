from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/')
def get_data():
    features = {
        {
            "type": "Feature",
            "geometry": {"type": "Point",
                         "coordinates": [102.0, 0.5]},
            "properties": {"name": "value0"}
        },
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
            "properties": {"name": "value0", "note": "note"}
        }
    }

    return jsonify(features)


if __name__ == '__main__':
    app.run()
