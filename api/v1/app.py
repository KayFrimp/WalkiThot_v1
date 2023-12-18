#!venv/bin/python3
"""API module with Flask"""
import os
from flask import Flask, jsonify, make_response
from flask_login import LoginManager

from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '01589' # Added a secret key
bcrypt = Bcrypt(app)

#Adding Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "app_views.login"
login_manager.login_message = "danger"

# Registering blueprints
from api.v1.views import app_views

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(arg):
    """ Closes Database Session """
    from models import storage
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ 404 error handler """
    return make_response(jsonify({"error": "Not found"}), 404)

# Reload user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    from models import storage
    return storage.get(User, user_id)


if __name__ == "__main__":
    """Runs only when script is the main program"""
    host = os.getenv('WALKI_API_HOST', default='0.0.0.0')
    port = os.getenv('WALKI_API_PORT', default=5000)
    app.run(host, int(port), threaded=True, debug=True)
