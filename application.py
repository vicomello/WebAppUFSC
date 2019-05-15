import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
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

lista = [0]


# Configure application - Copied from Problem set 8
app = Flask(__name__)

# Ensure templates are auto-reloaded - Copied from Problem set 8
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies) - Copied from problem set 8
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure responses aren't cached - Copied from Problem set 8


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies) - Copied from Problem set 8
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///appeople.db")

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

        if not request.form.get("email"):
            return apology("You must provide a valid email.")

        if not request.form.get("password"):
            return apology("You must provide a password.")

        if not request.form.get("confirmation"):
            return apology("You must confirm your password.")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Your passwords don't match! Try typing again.")

        users = db.execute("SELECT username FROM users WHERE username = :username", username=request.form.get("username"))
        if not users:
            hashword = generate_password_hash(request.form.get("password"))
            users = db.execute("INSERT INTO users (username, hashword, email) VALUES(:username, :hash, :email)",
                               username=request.form.get("username"), hash=hashword, email=request.form.get("email"))
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=request.form.get("username"))
            session["user_id"] = rows[0]["user_id"]
            return redirect("/index")

        elif True:
            return apology("Username was already taken!")

# Renders our blog page


@app.route("/", methods=["GET"])
def blog():
    return render_template("blog_3.html")


# Gets data from user lifestyle and interests
@app.route("/lifestyle", methods=["GET", "POST"])
@login_required
def lifestyle():
    if request.method == "GET":
        return render_template("lifestyle.html")
        #session["user_id"]

    if request.method == "POST":


        if request.form.get("lf1"):
            lf1 = 1
        else:
            lf1 = 0

        if request.form.get("lf2"):
            lf2 = 1
        else:
            lf2 = 0

        if request.form.get("lf3"):
            lf3 = 1
        else:
            lf3 = 0

        if request.form.get("lf4"):
            lf4 = 1
        else:
            lf4 = 0

        if request.form.get("lf5"):
            lf5 = 1
            esportes = request.form.get("esportes")
        else:
            lf5 = 0
            esportes = "NULL"

        if request.form.get("lf6"):
            lf6 = 1
            jogos = request.form.get("jogos")
        else:
            lf6 = 0
            jogos = "NULL"

        if request.form.get("lf7"):
            lf7 = 1
            eventos = request.form.get("eventos")
        else:
            lf7 = 0
            eventos = "NULL"

        if request.form.get("lf8"):
            lf8 = 1
            arte = request.form.get("arte")
        else:
            lf8 = 0
            arte = "NULL"

        if request.form.get("lf9"):
            lf9 = 1
        else:
            lf9 = 0

        if request.form.get("lf10"):
            lf10 = 1
        else:
            lf10 = 0

        if request.form.get("lf11"):
            lf11 = 1
        else:
            lf11 = 0

        if request.form.get("lf12"):
            lf12 = 1
        else:
            lf12 = 0

        if request.form.get("lf13"):
            lf13 = 1
        else:
            lf13 = 0

        if request.form.get("lf14"):
            lf14 = 1
            religiao = request.form.get("religiao")
        else:
            lf14 = 0
            religiao = "NULL"

        if request.form.get("lf15"):
            lf15 = 1
        else:
            lf15 = 0

        if request.form.get("lf16"):
            lf16 = 1
        else:
            lf16 = 0

        if request.form.get("lf17"):
            lf17 = 1
        else:
            lf17 = 0

        if request.form.get("lf18"):
            lf18 = 1
            ar_livre = request.form.get("ar_livre")
        else:
            lf18 = 0
            ar_livre = "NULL"

        if request.form.get("lf19"):
            lf19 = 1
            manuais = request.form.get("manuais")
        else:
            lf19 = 0
            manuais = "NULL"

        if request.form.get("lf20"):
            lf20 = 1
            estudos = request.form.get("estudos")
        else:
            lf20 = 0
            estudos = "NULL"

        if request.form.get("lf21"):
            lf21 = 1
        else:
            lf21 = 0

        if request.form.get("lf22"):
            lf22 = 1
        else:
            lf22 = 0

        if request.form.get("lf23"):
            lf23 = 1
        else:
            lf23 = 0

        if request.form.get("lf24"):
            lf24 = 1
        else:
            lf24 = 0

        # Checking if user is already in "traits" table or if he is inputing his interests for the first time
        user = db.execute("SELECT user_id FROM traits where user_id = :user_id", user_id=session["user_id"])
        if not user:
            db.execute("INSERT INTO traits (lf1, lf2, lf3, lf4, lf5, lf6, lf7, lf8, lf9, lf10, lf11, lf12, lf13, lf14,"
                       "lf15, lf16 ,lf17, lf18, lf19, lf20, lf21, lf22, lf23, lf24, esportes, jogos, eventos, arte,"
                       " religiao, ar_livre, manuais, estudos, user_id) VALUES (:lf1, :lf2, :lf3, "
                       ":lf4, :lf5, :lf6, :lf7, :lf8, :lf9, :lf10, :lf11, :lf12, :lf13, :lf14, :lf15,:lf16, :lf17, "
                       ":lf18, :lf19, :lf20, :lf21, :lf22, :lf23, :lf24, :esportes, :jogos, :eventos, :arte, :religiao, "
                       ":ar_livre, :manuais, :estudos, :user_id)",
                       lf1=lf1, lf2=lf2, lf3=lf3, lf4=lf4, lf5=lf5, lf6=lf6, lf7=lf7, lf8=lf8, lf9=lf9, lf10=lf10,
                       lf11=lf11, lf12=lf12, lf13=lf13, lf14=lf14, lf15=lf15, lf16=lf16, lf17=lf17, lf18=lf18,
                       lf19=lf19, lf20=lf20, lf21=lf21, lf22=lf22, lf23=lf23, lf24=lf24, esportes=esportes, jogos=jogos,
                       eventos=eventos, arte=arte, religiao=religiao, ar_livre=ar_livre, manuais=manuais,
                       estudos=estudos, user_id=session["user_id"])
            return redirect("/index")
        else:
            db.execute("UPDATE traits SET lf1=:lf1, lf2=:lf2, lf3=:lf3, lf4=:lf4, lf5=:lf5, lf6=:lf6, lf7=:lf7, "
                       "lf8=:lf8, lf9=:lf9, lf10=:lf10, lf11=:lf11, lf12=:lf12, lf13=:lf13, lf14=:lf14, lf15=:lf15, "
                       "lf16=:lf16, lf17=:lf17, lf18=:lf18, lf19=:lf19, lf20=:lf20, lf21=:lf21, lf22=:lf22, lf23=:lf23, "
                       "lf24=:lf24, esportes=:esportes, jogos=:jogos, eventos=:eventos, arte=:arte, religiao=:religiao,"
                       "ar_livre=:ar_livre, manuais=:manuais, estudos=:estudos WHERE user_id= :user_id",
                       lf1=lf1, lf2=lf2, lf3=lf3, lf4=lf4, lf5=lf5, lf6=lf6, lf7=lf7, lf8=lf8, lf9=lf9, lf10=lf10,
                       lf11=lf11, lf12=lf12, lf13=lf13, lf14=lf14, lf15=lf15, lf16=lf16, lf17=lf17, lf18=lf18,
                       lf19=lf19, lf20=lf20, lf21=lf21, lf22=lf22, lf23=lf23, lf24=lf24,esportes=esportes, jogos=jogos,
                       eventos=eventos, arte=arte, religiao=religiao, ar_livre=ar_livre, manuais=manuais,
                       estudos=estudos, user_id=session["user_id"])
            return redirect("/index")


# Renders index page
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html")


@app.route("/check", methods=["GET"])
def check():

    #Return true if username available, else false, in JSON format. Copied from Problem Set 8

    username = request.args.get("username")
    rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

    # If inputed username does not have at least 1 character and is not taken
    if len(username) > 1 and not rows:
        return jsonify(True)

    else:
        return jsonify(False)

# Login function - copied from Problem set 8


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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hashword"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]

        # Redirect user to home page
        return redirect("/index")

# This is the algorithm that matches the user with someone else highly compatible


@app.route("/match", methods=["GET", "POST"])
@login_required
def match():

    # Get the personality data from the user
    if request.method == "GET":

        # Gets the user's data about his interests/lifestyle
        lf1 = db.execute("SELECT lf1 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf1']
        lf2 = db.execute("SELECT lf2 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf2']
        lf3 = db.execute("SELECT lf3 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf3']
        lf4 = db.execute("SELECT lf4 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf4']
        lf5 = db.execute("SELECT lf5 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf5']
        lf6 = db.execute("SELECT lf6 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf6']
        lf7 = db.execute("SELECT lf7 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf7']
        lf8 = db.execute("SELECT lf8 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf8']
        lf9 = db.execute("SELECT lf9 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf9']
        lf10 = db.execute("SELECT lf10 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf10']
        lf11 = db.execute("SELECT lf11 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf11']
        lf12 = db.execute("SELECT lf12 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf12']
        lf13 = db.execute("SELECT lf13 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf13']
        lf14 = db.execute("SELECT lf14 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf14']
        lf15 = db.execute("SELECT lf15 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf15']
        lf16 = db.execute("SELECT lf16 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf16']
        lf17 = db.execute("SELECT lf17 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf17']
        lf18 = db.execute("SELECT lf18 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf18']
        lf19 = db.execute("SELECT lf19 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf19']
        lf20 = db.execute("SELECT lf20 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf20']
        lf21 = db.execute("SELECT lf21 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf21']
        lf22 = db.execute("SELECT lf22 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf22']
        lf23 = db.execute("SELECT lf23 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf23']
        lf24 = db.execute("SELECT lf24 FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['lf24']

        # Creates a list of dicts for every lifestyle item consisting in all the users that have marked the same response

        lifestyle1 = db.execute("SELECT user_id FROM traits WHERE lf1=:lf1", lf1=lf1)
        lifestyle2 = db.execute("SELECT user_id FROM traits WHERE lf2=:lf2", lf2=lf2)
        lifestyle3 = db.execute("SELECT user_id FROM traits WHERE lf3=:lf3", lf3=lf3)
        lifestyle4 = db.execute("SELECT user_id FROM traits WHERE lf4=:lf4", lf4=lf4)
        lifestyle5 = db.execute("SELECT user_id FROM traits WHERE lf5=:lf5", lf5=lf5)
        lifestyle6 = db.execute("SELECT user_id FROM traits WHERE lf6=:lf6", lf6=lf6)
        lifestyle7 = db.execute("SELECT user_id FROM traits WHERE lf7=:lf7", lf7=lf7)
        lifestyle8 = db.execute("SELECT user_id FROM traits WHERE lf8=:lf8", lf8=lf8)
        lifestyle9 = db.execute("SELECT user_id FROM traits WHERE lf9=:lf9", lf9=lf9)
        lifestyle10 = db.execute("SELECT user_id FROM traits WHERE lf10=:lf10", lf10=lf10)
        lifestyle11 = db.execute("SELECT user_id FROM traits WHERE lf11=:lf11", lf11=lf11)
        lifestyle12 = db.execute("SELECT user_id FROM traits WHERE lf12=:lf12", lf12=lf12)
        lifestyle13 = db.execute("SELECT user_id FROM traits WHERE lf13=:lf13", lf13=lf13)
        lifestyle14 = db.execute("SELECT user_id FROM traits WHERE lf14=:lf14", lf14=lf14)
        lifestyle15 = db.execute("SELECT user_id FROM traits WHERE lf15=:lf15", lf15=lf15)
        lifestyle16 = db.execute("SELECT user_id FROM traits WHERE lf16=:lf16", lf16=lf16)
        lifestyle17 = db.execute("SELECT user_id FROM traits WHERE lf17=:lf17", lf17=lf17)
        lifestyle18 = db.execute("SELECT user_id FROM traits WHERE lf18=:lf18", lf18=lf18)
        lifestyle19 = db.execute("SELECT user_id FROM traits WHERE lf19=:lf19", lf19=lf19)
        lifestyle20 = db.execute("SELECT user_id FROM traits WHERE lf20=:lf20", lf20=lf20)
        lifestyle21 = db.execute("SELECT user_id FROM traits WHERE lf21=:lf21", lf21=lf21)
        lifestyle22 = db.execute("SELECT user_id FROM traits WHERE lf22=:lf22", lf22=lf22)
        lifestyle23 = db.execute("SELECT user_id FROM traits WHERE lf23=:lf23", lf23=lf23)
        lifestyle24 = db.execute("SELECT user_id FROM traits WHERE lf24=:lf24", lf24=lf24)

        # Appends all those users that had things in common to one list
        for item in lifestyle1:
            lista.append(item['user_id'])
        for item in lifestyle2:
            lista.append(item['user_id'])
        for item in lifestyle3:
            lista.append(item['user_id'])
        for item in lifestyle4:
            lista.append(item['user_id'])
        for item in lifestyle5:
            lista.append(item['user_id'])
        for item in lifestyle6:
            lista.append(item['user_id'])
        for item in lifestyle7:
            lista.append(item['user_id'])
        for item in lifestyle8:
            lista.append(item['user_id'])
        for item in lifestyle9:
            lista.append(item['user_id'])
        for item in lifestyle10:
            lista.append(item['user_id'])
        for item in lifestyle11:
            lista.append(item['user_id'])
        for item in lifestyle12:
            lista.append(item['user_id'])
        for item in lifestyle13:
            lista.append(item['user_id'])
        for item in lifestyle14:
            lista.append(item['user_id'])
        for item in lifestyle15:
            lista.append(item['user_id'])
        for item in lifestyle16:
            lista.append(item['user_id'])
        for item in lifestyle17:
            lista.append(item['user_id'])
        for item in lifestyle18:
            lista.append(item['user_id'])
        for item in lifestyle19:
            lista.append(item['user_id'])
        for item in lifestyle20:
            lista.append(item['user_id'])
        for item in lifestyle21:
            lista.append(item['user_id'])
        for item in lifestyle22:
            lista.append(item['user_id'])
        for item in lifestyle23:
            lista.append(item['user_id'])
        for item in lifestyle24:
            lista.append(item['user_id'])

        # Calculating which user appears the most number of times
        user_id = session["user_id"]
        # Removes the own user (loged in) from the list
        nova = [x for x in lista if x != user_id]
        # Calculates the mode in that list
        partner = max(set(nova), key=nova.count)
        # Get the user's info based on their user_id
        name = db.execute("SELECT username, email FROM users WHERE user_id=:user_id", user_id=partner)
        # Render the results of who is the highest matching person
        return render_template("personality_results.html", name=name)


# Log out function - copied from Problem Set 8
@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
