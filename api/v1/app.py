#!venv/bin/python3
"""API module with Flask"""
import os
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(arg):
    """ Closes Database Session """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ 404 error handler """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    """Runs only when script is the main program"""
    host = os.getenv('WALKI_API_HOST', default='0.0.0.0')
    port = os.getenv('WALKI_API_PORT', default=5000)
    app.run(host, int(port), threaded=True, debug=True)
