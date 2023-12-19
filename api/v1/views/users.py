#!venv/bin/python3
"""USER RESTFul API Definitions"""
from flask import Blueprint, abort, jsonify, request
# from api.v1.views import app_views

user_bp = Blueprint("users", __name__)


@user_bp.route('/users', methods=['GET'], strict_slashes=False)
def fetch_all_users():
    """API Fetches all User objects from the DB"""
    from models import storage
    from models.user import User
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)


@user_bp.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def fetch_user(user_id):
    """API Fetches User object by id"""
    from models import storage
    from models.user import User
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@user_bp.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """API deletes User object by id"""
    from models import storage
    from models.user import User
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@user_bp.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """API creates a new User object in DB"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'email' not in request.get_json():
        abort(400, 'Missing email')
    if 'password' not in request.get_json():
        abort(400, 'Missing password')
    if 'first_name' not in request.get_json():
        abort(400, 'Missing first name')
    attributes = request.get_json()
    from models import storage
    from models.user import User
    user = User(**attributes)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201


@user_bp.route('/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """API updates User object by id"""
    from models import storage
    from models.user import User
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    attributes = request.get_json()
    for key, value in attributes.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict()), 200


