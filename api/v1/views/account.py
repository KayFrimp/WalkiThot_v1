from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from api.v1.forms.user_account_forms import RegisterForm, LoginForm

accounts_bp = Blueprint("accounts", __name__)


# Added the view for Registering a user
@accounts_bp.route('/register', methods=["GET", "POST"], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        from models.user import User
        from models import storage
        users = [user for user in storage.all(User).values() if user.email == form.email.data]
        user = users[0] if users else None
        if user:
            flash("Email already exists!", "danger")
            return render_template("/register.html", form=form)
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            cohort=form.cohort.data,
            password=form.password.data
        )
        storage.new(user)
        storage.save()

        login_user(user)
        flash("You registered and are now logged in. Welcome!", "success")

        return redirect(url_for("core.home"))
    return render_template("/register.html", form=form)


# Added the view for User Login
@accounts_bp.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        from models import storage
        from models.user import User
        users = [user for user in storage.all(User).values() if user.email == form.email.data]
        user = users[0] if users else None
        from api.v1.app import bcrypt
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("core.home"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("/login.html", form=form)
    return render_template("/login.html", form=form)

@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("core.home"))