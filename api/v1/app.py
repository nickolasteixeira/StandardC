#!/usr/bin/python3
'''Basic Flask Application'''
from flask import Flask, Blueprint, make_response, jsonify
from os import getenv
from api.v1.views import app_views
from flask_cors import CORS
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    env_var = {'host': '0.0.0.0', 'port': 5000}
    if getenv('API_HOST'):
        env_var['host'] = getenv('API_HOST')
    if getenv('API_PORT'):
        env_var['port'] = int(getenv('API_PORT'))
    app.run(host=env_var.get('host'), port=env_var.get('port'), threaded=True)
