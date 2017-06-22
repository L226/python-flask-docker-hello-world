"""
Basic app to test terraformed infrastructure on AWS.
- ALB (80, 443) -> dynamic port
- ECS dynamic port -> 8080 (container port)
- Flask API (gunicorn)

"""
from flask import Flask
from flask_restful import Api
from flask import Response
import json

app = Flask(__name__)
api = Api(app)

@app.route('/')
def api_root():
    """
    """
    return Response(json.dumps('hello world'), status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)
