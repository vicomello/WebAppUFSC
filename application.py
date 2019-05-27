import os

from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
import sys
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter
from timeit import timeit
import smtplib

from helpers import login_required, apology

lista = list()
traits_db_fields = ['lf1', 'lf2', 'lf3', 'lf4', 'lf5', 'lf6', 'lf7', 'lf8', 'lf9', 'lf10', 'lf11', 'lf12',
                            'lf13', 'lf14', 'lf15', 'lf16', 'lf17', 'lf18', 'lf19', 'lf20', 'lf21', 'lf22', 'lf23',
                            'lf24', 'esportes', 'jogos', 'eventos', 'arte', 'religiao', 'ar_livre', 'manuais',
                            'estudos']


# Configure application - Copied from Problem set 8
app = Flask(__name__)

# Ensure templates are auto-reloaded - Copied from Problem set 8
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies) - Copied from problem set 8
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# setting the database directory
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///appeople.db"

Session(app)
# connecting to the database
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)
# Ensure responses aren't cached - Copied from Problem set 8


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies) - Copied from Problem set 8

Session(app)


class User(db.Model):
    __table__ = db.Model.metadata.tables['users']

    def __init__(self, username, hashword, email):
        self.username = username
        self.hashword = hashword
        self.email = email

class Itens(db.Model):
    __table__ = db.Model.metadata.tables['itens']

    def __init__(self, lf1, lf2, lf3, lf4, lf5, lf6, lf7, lf8, lf9, lf10, lf11, lf12, lf13, lf14, lf15, lf16, lf17, lf18, lf19, lf20, lf21, lf22, lf23, lf24, esportes, jogos, eventos, arte, religiao, ar_livre, manuais, estudos):
        self.lf1 = lf1
        self.lf2 = lf2
        self.lf3 = lf3
        self.lf4 = lf4
        self.lf5 = lf5
        self.lf6 = lf6
        self.lf7 = lf7
        self.lf8 = lf8
        self.lf9 = lf9
        self.lf10 = lf10
        self.lf11 = lf11
        self.lf12 = lf12
        self.lf13 = lf13
        self.lf14 = lf14
        self.lf15 = lf15
        self.lf16 = lf16
        self.lf17 = lf17
        self.lf18 = lf18
        self.lf19 = lf19
        self.lf20 = lf20
        self.lf21 = lf21
        self.lf22 = lf22
        self.lf23 = lf23
        self.lf24 = lf24
        self.esportes = esportes
        self.jogos = jogos
        self.eventos = eventos
        self.arte = arte
        self.religiao = religiao
        self.ar_livre = ar_livre
        self.manuais = manuais
        self.estudos = estudos

class Traits(db.Model):
    __table__ = db.Model.metadata.tables['traits']

    def __init__(self, lf1, lf2, lf3, lf4, lf5, lf6, lf7, lf8, lf9, lf10, lf11, lf12, lf13, lf14, lf15, lf16, lf17, lf18, lf19, lf20, lf21, lf22, lf23, lf24, esportes, jogos, eventos, arte, religiao, ar_livre, manuais, estudos, user_id):
        self.lf1 = lf1
        self.lf2 = lf2
        self.lf3 = lf3
        self.lf4 = lf4
        self.lf5 = lf5
        self.lf6 = lf6
        self.lf7 = lf7
        self.lf8 = lf8
        self.lf9 = lf9
        self.lf10 = lf10
        self.lf11 = lf11
        self.lf12 = lf12
        self.lf13 = lf13
        self.lf14 = lf14
        self.lf15 = lf15
        self.lf16 = lf16
        self.lf17 = lf17
        self.lf18 = lf18
        self.lf19 = lf19
        self.lf20 = lf20
        self.lf21 = lf21
        self.lf22 = lf22
        self.lf23 = lf23
        self.lf24 = lf24
        self.esportes = esportes
        self.jogos = jogos
        self.eventos = eventos
        self.arte = arte
        self.religiao = religiao
        self.ar_livre = ar_livre
        self.manuais = manuais
        self.estudos = estudos
        self.user_id = user_id


# Register new user - Copied from Problem set 8
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Render register page
    if request.method == "GET":
        return render_template("register.html")

    # Checking if user provided all the required fields correctly and if the username is taken
    elif request.method == "POST":
        if not request.form.get("username"):
            return apology("You must provide a username.")
        else:
            username = request.form['username']

        if not request.form.get("email"):
            return apology("You must provide a valid email.")
        else:
            email = request.form['email']

        if not request.form.get("password"):
            return apology("You must provide a password.")
        else:
            password = request.form['password']

        if not request.form.get("confirmation"):
            return apology("You must confirm your password.")

        if password != request.form.get("confirmation"):
            return apology("Your passwords don't match! Try typing again.")

        if not User.query.filter_by(username=username).all():

            user = User(username=username, hashword=generate_password_hash(password), email=email)
            db.session.add(user)
            db.session.commit()

            user_id = User.query.filter_by(username=username).first().user_id
            session["user_id"] = user_id
            return redirect("/index")

        elif True:
            return apology("Username is already taken!")

# Renders our blog page
@app.route("/", methods=["GET"])
def blog():
    return render_template("blog_3.html")

# Renders index page
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html")


# Gets data from user lifestyle and interests
@app.route("/lifestyle", methods=["GET", "POST"])
@login_required
def lifestyle():
    if request.method == "GET":
        return render_template("lifestyle.html")

    elif request.method == "POST":
        """traits_db_fields = ['lf1', 'lf2', 'lf3', 'lf4', 'lf5', 'lf6', 'lf7', 'lf8', 'lf9', 'lf10', 'lf11', 'lf12',
                            'lf13', 'lf14', 'lf15', 'lf16', 'lf17', 'lf18', 'lf19', 'lf20', 'lf21', 'lf22', 'lf23',
                            'lf24', 'esportes', 'jogos', 'eventos', 'arte', 'religiao', 'ar_livre', 'manuais',
                            'estudos']"""
        traits_dict = dict()
        for field in traits_db_fields:
            response = request.form.get(field)
            # checks if response exists (not filled in the form)
            if response:
                # if response is not "1" , its database value will be response itself
                if len(response) > 1:
                    traits_dict[field] = response
                # on the other hand, it will be True(Boolean)
                else:
                    traits_dict[field] = 1
            # if response doesn't exists, database value will be 0
            else:
                traits_dict[field] = 0

        traits_dict['user_id'] = session['user_id']

        # Checking if user is already in "traits" table or if he is inputing his interests for the first time

        user = Traits.query.filter_by(user_id=session['user_id']).first()
        if not user:

            traits_entry = Traits(**traits_dict)
            db.session.add(traits_entry)
            db.session.commit()

            return redirect("/index")
        else:
            # iterate through keys and values of a dictionary
            for key, value in traits_dict.items():
                # setattr(object (observation), attribute, value)
                setattr(user, key, value)
            db.session.commit()
            return redirect("/index")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():

    if request.method == "GET":
        users_new_fields = ['name', 'age', 'sex', 'curso', 'top_1', 'top_2', 'top_3', 'ice_breaker', 'sexes']


        # auxilary dictionary
        users_dict = dict()

        query = User.query.filter_by(user_id=session['user_id']).first()
        for field in users_new_fields:
            users_dict[field] = getattr(query, field)


        query_traits = Traits.query.filter_by(user_id=session['user_id']).first()
        query_itens = Itens.query.first()
        questions = dict()

        for element in traits_db_fields:
            if getattr(query_traits, element) is True:
                    questions[element] = getattr(query_itens, element)

        marked = questions.values()
        print("\n\n\n\n\n")
        print(marked)
        print("\n\n\n\n\n")

        return render_template("profile.html", **users_dict, marked=marked)

    elif request.method == "POST":

        # list of reference for fields used
        users_new_fields = ['name', 'age', 'sex', 'curso', 'top_1', 'top_2', 'top_3', 'ice_breaker', 'sexes']


        # auxilary dictionary
        users_dict = dict()

        for field in users_new_fields:
            response = request.form.get(field)
            users_dict[field] = response

        print(users_dict)

        users_dict['user_id'] = session['user_id']
        user = User.query.filter_by(user_id=session['user_id']).first()

        for key, value in users_dict.items():
            setattr(user, key, value)
        db.session.commit()

        query = User.query.filter_by(user_id=session['user_id']).first()
        for field in users_new_fields:
            users_dict[field] = getattr(query, field)

        questions = dict()
        query_traits = Traits.query.filter_by(user_id=session['user_id']).first()
        query_itens = Itens.query.first()

        for element in traits_db_fields:
            if getattr(query_traits, element) is True:
                questions[element] = getattr(query_itens, element)

        marked = questions.values()

        return render_template("profile.html", **users_dict, marked=marked)


@app.route("/check", methods=["GET"])
def check():

    #Return true if username available, else false, in JSON format. Copied from Problem Set 8

    username = request.args.get("username")
    rows = User.query.filter_by(username=username).all()

    # If inputed username does not have at least 1 character and is not taken
    if len(username) > 1 and not rows:
        return jsonify(True)
    else:
        return jsonify(False)

# Login function - copied from Problem set 8

@app.route("/rascunho", methods=["GET", "POST"])
def rascunho():
    if request.method == "GET":
        return render_template("rascunho2.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = User.query.filter_by(username=request.form.get("username")).all()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0].hashword, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0].user_id

        # Redirect user to home page
        return redirect("/index")

# This is the algorithm that matches the user with someone else highly compatible


@app.route("/match", methods=["GET", "POST"])
@login_required
def match():

    # Get the personality data from the user
    if request.method == "GET":

        # Gets the user's data about his interests/lifestyle
        lf_dict = dict()
        lifestyle_dict = dict()
        for i in range(1, 25):
            lf_key = 'lf{}'.format(i)
            lf_dict[lf_key] = getattr(Traits.query.filter_by(user_id=session['user_id']).all()[0], lf_key)

            # Creates a list of dicts for every lifestyle item consisting in all the users that have marked the same response
            dicionario={}
            dicionario[lf_key] = lf_dict[lf_key]

            keys_in_traits = Traits.query.filter_by(**dicionario).all()

            lfkey_user_id = []
            for key in keys_in_traits:
                lfkey_user_id.append(key.user_id)

            lifestyle_dict[lf_key] = lfkey_user_id

            #db.execute("SELECT user_id FROM traits WHERE {}=:parameter".format(lf_key), parameter=lf_dict[lf_key])

            # Appends all those users that had things in common to one list
            for item in lifestyle_dict[lf_key]:
                lista.append(item)

        # Removes the own user (logged in) from the list
        nova = [x for x in lista if x != session["user_id"]]

        # Calculating which user appears the most number of times using the mode in that list
        partner = max(set(nova), key=nova.count)

        # Get the user's info based on their user_id
        name = getattr(User.query.filter_by(user_id=partner).first(), "username")
        email = getattr(User.query.filter_by(user_id=partner).first(), "email")

            #db.execute("SELECT username, email FROM users WHERE user_id=:user_id", user_id=partner)

        # Render the results of who is the highest matching person
        return render_template("to-match.html", name=name, email=email)


# Log out function - copied from Problem Set 8
@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
