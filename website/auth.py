from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


# Define blueprint
auth = Blueprint('auth', __name__)


@auth.route("/")
def index():

    # Check if user is already logged in
    if current_user.is_authenticated:

        # Redirect user to home page
        return redirect(url_for("views.home"))

    else:

        # Display index page
        return render_template("index.html")


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Collect form information
        email = request.form.get("email")
        password = request.form.get("password")

        # Query database for user
        user = User.query.filter_by(email=email).first()

        # Ensure email was submitted
        if not email:
            flash("Must provide an email address.", category="error")
        
        # Ensure password was submitted
        elif not password:
            flash("Must provide a password.", category="error")

        # Ensure email is in database
        elif user:

            # Ensure password matches
            if check_password_hash(user.password, password):

                # Log user in
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            
            else:
                flash("Incorrect password. Try again.", category="error")

        else:
            flash("Email does not exist.", category="error")

    # Display form to user
    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():

    # Log user out
    logout_user()

    # Redirect user to index page
    return redirect(url_for("auth.index"))


@auth.route('/create-account', methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # Collect form information
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Query database for user
        user = User.query.filter_by(email=email).first()

        # Ensure email was submitted
        if not email:
            flash("Must provide an email address.", category="error")

        # Ensure email doesn't already exist
        elif user:
            flash("Email already exists.", category="error")

        # Ensure password was submitted
        elif not password:
            flash("Must provide a password.", category="error")

        # Ensure confirmation was submitted
        elif not confirmation:
            flash("Must confirm the password", category="error")

        # Ensure password and confirmation match
        elif password != confirmation:
            flash("Passwords don't match.", category="error")

        # Add user to database
        else:
            new_user = User(email=email, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            # Log user in
            login_user(new_user, remember=True)

            # Redirect user to home page
            return redirect(url_for("views.home"))

    # Display form to user
    return render_template("register.html")