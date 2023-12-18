#!venv/bin/python3
"""USER RESTFul API Definitions"""
from flask import abort, flash, jsonify, redirect, render_template, request, url_for
from api.v1.views import app_views
from flask_login import current_user, login_required, login_user, logout_user
from api.v1.forms.user_account_forms import LoginForm, RegisterForm
from api.v1.app import bcrypt
from models import storage
from models.user import User


# Added the view for Registering a user
@app_views.route('/register', methods=["GET", "POST"], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            cohort=form.cohort.data,
            password=form.password.data
        )
        storage.new(user)
        storage.save(user)

        login_user(user)
        flash("You registered and are now logged in. Welcome!", "success")

        return redirect(url_for("home"))
    return render_template("/register.html", form=form)


# Added the view for User Login
@app_views.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        users = [user for user in storage.all(User).values() if user.email == form.email.data]
        user = users[0] if users else None
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("/login.html", form=form)
    return render_template("/login.html", form=form)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def fetch_all_users():
    """API Fetches all User objects from the DB"""
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def fetch_user(user_id):
    """API Fetches User object by id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """API deletes User object by id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
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
    user = User(**attributes)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """API updates User object by id"""
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


@app_views.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("login"))
