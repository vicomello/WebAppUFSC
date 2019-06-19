import os

from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
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
one_way_match = list()
one_way_dict = dict()
traits_db_fields = ['lf1', 'lf2', 'lf3', 'lf4', 'lf5','esportes', 'lf6', 'jogos', 'lf7', 'eventos', 'lf8', 'arte',
                    'lf9', 'lf10', 'lf11', 'lf12', 'lf13', 'lf14', 'religiao', 'lf15', 'lf16', 'lf17', 'lf18',
                    'ar_livre', 'lf19', 'manuais', 'lf20', 'estudos', 'lf21', 'lf22', 'lf23', 'lf24']

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

class Matches(db.Model):
    __table__ = db.Model.metadata.tables['matches']

    def __init__(self, user_id, match1, match2, match3, match4, match5, match6, match7, match8, match9, match10, match11, match12, match13, match14, match15, match16, match17, match18, match19, match20):
        self.user_id = user_id
        self.match1 = match1
        self.match2 = match2
        self.match3 = match3
        self.match4 = match4
        self.match5 = match5
        self.match6 = match6
        self.match7 = match7
        self.match8 = match8
        self.match9 = match9
        self.match10 = match10
        self.match11 = match11
        self.match12 = match12
        self.match13 = match13
        self.match14 = match14
        self.match15 = match15
        self.match16 = match16
        self.match17 = match17
        self.match18 = match18
        self.match19 = match19
        self.match20 = match20

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
        query = Traits.query.filter_by(user_id=session['user_id']).first()

        questions = dict()

        if query:
            for item in traits_db_fields:
                questions[item] = getattr(query, item)
        else:
            for item in traits_db_fields:
                questions[item] = 0


        sports = ['futebol', 'vôlei', 'handebol', 'basquete', 'tênis', 'corrida', 'musculação', 'surf', 'natação', 'outro']
        games = ['League of Legends', 'Dota', 'WOW', 'CS', 'Outro']
        events = ['Shows', 'Teatro', 'Exposições de Arte', 'Performances de Dança', 'Cinema', 'Outro']
        art = ['Música', 'Artes Visuais', 'Dança', 'Fotografia', 'Literatura', 'Teatro']
        religion = ['Missa Católica', 'Centro Espírita', 'Outro']
        air = ['trilhas', 'acampar', 'meditar', 'outro']
        manuals = ['jardinagem', 'marcenaria', 'outro']
        studies = ['estudos em ciências sociais', 'estudos em ciências exatas', 'estudos em literatura', 'estudos sobre arte', 'estudos em línguas estrangeiras', 'outro']



        return render_template("lifestyle.html", **questions, sports=sports, games=games, events=events, art=art,
                               religion=religion, air=air, manuals=manuals, studies=studies)

    elif request.method == "POST":

        # ==================== PART 1: GET GENERAL INFO FROM FIELDS IN PROFILE AND POST IT IN DB ====================

        quali_dict = dict()
        traits_dict = dict()

        # For loop inserting info into dicts
        for field in range(len(traits_db_fields)):
            response = request.form.get('{}'.format(traits_db_fields[field]))
            # checks if response exists (not filled in the form)
            if response:
                # if response is not "1" , its database value will be response itself
                if len(response) > 1:
                    traits_dict[traits_db_fields[field]] = response
                    quali_dict[traits_db_fields[field-1]] = response
                # on the other hand, it will be True(Boolean)
                else:
                    traits_dict[traits_db_fields[field]] = 1
            # if response doesn't exists, database value will be 0
            else:
                traits_dict[traits_db_fields[field]] = 0

        traits_dict['user_id'] = session['user_id']

        user = Traits.query.filter_by(user_id=session['user_id']).first()

        # Checking if user is already in "traits" table or if he is inputing his interests for the first time
        if not user:

            traits_entry = Traits(**traits_dict)
            db.session.add(traits_entry)
            db.session.commit()

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

        # ==================== PART 1 - DISPLAY INFO FROM PROFILE PAGE GIVEN BY USER ====================

        # Fields in profile page
        users_new_fields = ['name', 'age', 'sex', 'curso', 'top_1', 'top_2', 'top_3', 'ice_breaker', 'sexes',
                            'facebook', 'top_1_text', 'top_2_text', 'top_3_text']

        # Querying from 3 different tables needed
        query = User.query.filter_by(user_id=session['user_id']).first()
        query_traits = Traits.query.filter_by(user_id=session['user_id']).first()
        query_itens = Itens.query.first()

        # Empty dict to store values from db
        users_dict = dict()
        # Storing data from table "Users" into dict
        for field in users_new_fields:
            users_dict[field] = getattr(query, field)

        # This dict will store the questions descriptions (e.g.: lf5: praticar esportes)
        questions = dict()
        # Turning items into questions descriptions
        for element in traits_db_fields:
            if getattr(query_traits, element) is True:
                questions[element] = getattr(query_itens, element)

        # List to be passed to display at profile page
        marked = questions.values()

        # ==================== PART 2: DISPLAYING ADDITIONAL INFO RELATED TO EACH ITEM ====================

        # Dict of item additional descriptions
        item_description_dict = {
                "Praticar esportes": 'esportes',
                "Jogar jogos eletrônicos": 'jogos',
                "Ir a eventos relacionados a arte": 'eventos',
                "Produzir arte comigo": 'arte',
                "Ir a eventos religiosos (culto, missa, etc)": 'religiao',
                "Realizar atividades ao ar livre": 'ar_livre',
                "Fazer trabalhos manuais": 'manuais',
                "Criar grupos de conversa ou de estudos": 'estudos'
             }

        # Dictionaire to store the values from the users interests description (e.x.: tênis)
        qualitative_descriptions = dict()
        # Creating list of items to iterate through (number 0 won't go)
        qualitative_list = ["trash", "top_1_item", "top_2_item", "top_3_item"]
        # Saving user additional info into dict
        for i in range(1, 4):
            itens_preenchidos = getattr(query, 'top_{}_item'.format(i))
            if itens_preenchidos:
                qualitative_descriptions[qualitative_list[i]] = itens_preenchidos

        lista_itens_preenchidos = list(qualitative_descriptions.values())

        return render_template("profile.html", **users_dict, marked=marked, **qualitative_descriptions, lista_itens_preenchidos=lista_itens_preenchidos)

    elif request.method == "POST":

        # ======================== PART 1: POSTING USER'S BASIC INFO FROM PROFILE INTO DB ========================

        # Fields to be posted into db
        users_new_fields = ['name', 'age', 'sex', 'curso', 'top_1', 'top_2', 'top_3', 'ice_breaker', 'sexes','facebook']
        # Auxilary dictionary to store info from those fields
        users_dict = dict()
        users_dict['user_id'] = session['user_id']
        for field in users_new_fields:
            response = request.form.get(field)
            users_dict[field] = response

        # Query from User table
        user = User.query.filter_by(user_id=session['user_id']).first()
        # Posting basic info into table Users
        for key, value in users_dict.items():
            setattr(user, key, value)
        db.session.commit()


        #for field in users_new_fields:
        #    users_dict[field] = getattr(query, field)


        # Auxiliary empty dict
        questions = dict()

        # Getting query
        query_traits = Traits.query.filter_by(user_id=session['user_id']).first()
        query_itens = Itens.query.first()

        for element in traits_db_fields:
            if getattr(query_traits, element) is True:
                questions[element] = getattr(query_itens, element)

        marked = questions.values()

        # ==================== PART 2: POSTING ADDITIONAL INFO INTO USERS TABLE ====================

        # This dict serves as reference to check either an item has description or not
        item_description_dict = {
            "Praticar esportes": 'esportes',
            "Jogar jogos eletrônicos": 'jogos',
            "Ir a eventos relacionados a arte": 'eventos',
            "Produzir arte comigo": 'arte',
            "Ir a eventos religiosos (culto, missa, etc)": 'religiao',
            "Realizar atividades ao ar livre": 'ar_livre',
            "Fazer trabalhos manuais": 'manuais',
            "Criar grupos de conversa ou de estudos": 'estudos'
        }

        # Dictionaire to store the values from the users interests description (e.x.: tênis)
        qualitative_descriptions = dict()
        # List to iterate through (number 0 won't go)
        qualitative_list = ["trash", "top_1_item", "top_2_item", "top_3_item"]
        # Querying from Users table
        query = User.query.filter_by(user_id=session['user_id']).first()
        # Iterating through dict to store the values the user has selected as top 3 activities
        for i in range(1, 4):
            top = getattr(query, 'top_{}'.format(i))
            if top in list(item_description_dict.keys()):
                hobby = item_description_dict['{}'.format(top)]
                qualitative_descriptions[qualitative_list[i]] = getattr(query_traits, hobby)

        # Commiting info into users table
        for key, value in qualitative_descriptions.items():
            # setattr(object (observation), attribute, value)
            setattr(user, key, value)
        db.session.commit()

        return render_template("profile.html", **users_dict, marked=marked, **qualitative_descriptions)
                               #list_of_quali=list_of_quali)   **dict_of_quali,



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

        #======================== PART 1: Fazer match com as principais caractetisticas (table users) ===========================

        # Variáveis que vão ser usadas na primeira parte do match
        profile_things = ['top_1', 'top_2', 'top_3']
        profile_items = ['top_1_item', 'top_2_item', 'top_3_item']
        items_to_query = ['top_1', 'top_2', 'top_3', 'top_1_item', 'top_2_item', 'top_3_item']
        # Querying
        user_id = session['user_id']
        user = User.query.filter_by(user_id=user_id).first()
        # Dict com as infos do user
        top_info_user = {x: getattr(user, x) for x in items_to_query}
        # Preferência de sexos (pegar base toda ou apenas aqueles com mesmo sexo)
        preference = getattr(user, 'sexes')

        # Querying com base na preferência
        sexo = getattr(user, 'sex')
        if preference == 0:
            query = User.query.filter_by(sex=sexo).all()
        elif preference == 1 and sexo == 1:
            query = User.query.filter(or_(User.sexes == 1, User.sex == 1))
        elif preference == 1 and sexo == 0:
            query = User.query.filter(or_(User.sexes == 1, User.sex == 0))

        if not query:
            return message("Siga os passos. 1)Preencha seus interesses 2) Preencha seu perfil 3)Veja as sugestões de pessoas")

        number_of_rows = -1
        for row in query:
            number_of_rows = number_of_rows + 1

        # Auxiliary dict
        compatibility_of_users = dict()
        # Auxiliary list
        people_in_order = list()

        # Get traits info from user
        lf_dict = dict()
        query_traits = Traits.query.filter_by(user_id=user_id).first()
        for i in range(1, 25):
            lf_key = 'lf{}'.format(i)
            lf_dict[lf_key] = getattr(query_traits, lf_key)

        # Loop compara cada pessoa na base com o user e retorna um grau de compatibilidade
        for row in query:
            row_id = getattr(row, 'user_id')
            if int(user_id) != int(row_id):
                compatibilidade = 0
                top_info_pessoa = {x: getattr(row, x) for x in items_to_query}
                for i in range(0, 3):
                    thing = profile_things[i]
                    item = profile_items[i]
                    for j in range(0, 3):
                        thing2 = profile_things[j]
                        if top_info_user[thing] == top_info_pessoa[thing2]:
                            compatibilidade = compatibilidade + 40 - (i*10) - (j*5)
                            if top_info_user[item] == top_info_pessoa[item]:
                                compatibilidade = compatibilidade + 20

                # ============================== PARTE 2: Outras variáveis de interesses ==============================

                query_traits_row = Traits.query.filter_by(user_id=row_id).first()
                if query_traits_row:
                    row_dict = dict()
                    for i in range(1, 25):
                        lf_key = 'lf{}'.format(i)
                        row_dict[lf_key] = getattr(query_traits_row, lf_key)

                    for i in range(1, 25):
                        if lf_dict['lf{}'.format(i)] == 1 and lf_dict['lf{}'.format(i)] == row_dict['lf{}'.format(i)]:
                            compatibilidade = compatibilidade + 2

                compatibility_of_users['{}'.format(row_id)] = compatibilidade
                x = ((v, k) for k, v in compatibility_of_users.items())
                x = sorted(x, reverse=True)

        info_list = ['name', 'age', 'curso', 'top_1', 'top_2', 'top_3', 'top_1_item', 'top_2_item', 'top_3_item',
                     'top_1_text', 'top_2_text', 'top_3_text', 'user_id']

        # ==================== PART 3: Retirar da lista as pessoas com as quais ele já marcou interesse ====================
        db_match = Matches.query.filter_by(user_id=user_id).first()
        db_match_list = list()
        if db_match:
            for i in range(1, 21):
                key = 'match{}'.format(i)
                mate = getattr(db_match, key)
                if mate != 0:
                    db_match_list.append(mate)

        top_people = list()
        for i in range(0, number_of_rows):
            id_person = (int(x[i][1]))
            if id_person not in db_match_list:
                people_in_order.append(x[i][1])
                query_top_people = User.query.filter_by(user_id=id_person).first()
                person = dict()
                for item in info_list:
                    person[item] = getattr(query_top_people, item)
                top_people.append(person)

        if len(top_people) == 0:
            message = "As sugestões de pessoas acabaram. Caso você ainda não tenha tendado se conectar com ninguém," \
                      " certifique-se de preencher os dados de seus interesses e suas informações de perfil. Caso já " \
                      "tenha dado match com todas as opções, você pode mudar suas preferências em interesses e perfil e" \
                      " tentar novamente."
        else:
            message = "Sucess"

        return render_template("to-match.html", top_people=top_people, message=message)

    elif request.method == "POST":

        # Getting the data already saved in matches table
        matches_table_data = Matches.query.filter_by(user_id=session['user_id']).first()
        if matches_table_data:
            for i in range(1, 21):
                key = 'match{}'.format(i)
                mate = getattr(matches_table_data, key)
                if mate != 0:
                    one_way_match.append(mate)

        # Getting new matches from match form
        person_id = request.form.get('person_id')
        if int(person_id) not in one_way_match:
            one_way_match.append(int(person_id))
        # Removing duplicates
        one_way = list(dict.fromkeys(one_way_match))

        one_way_dict['user_id'] = session['user_id']
        for i in range(0, 20):
            match_key = 'match{}'.format(i+1)
            if len(one_way) > i:
                one_way_dict[match_key] = one_way[i]
            else:
                one_way_dict[match_key] = 0

        user = Matches.query.filter_by(user_id=session['user_id']).first()
        if not user:
            matches_entry = Matches(**one_way_dict)
            db.session.add(matches_entry)
            db.session.commit()
        else:
            # iterate through keys and values of a dictionary
            for key, value in one_way_dict.items():
                # setattr(object (observation), attribute, value)
                setattr(user, key, value)
            db.session.commit()

        return redirect("/match")


@app.route("/matched", methods=["GET", "POST"])
@login_required
def matched():
    if request.method == "GET":
        user_id = session['user_id']
        matches_query = Matches.query.filter_by(user_id=user_id).first()
        match_keys = list()
        matches = dict()
        for i in range(1, 21):
            match_key = "match{}".format(i)
            if matches_query:
                matches[match_key] = getattr(matches_query, match_key)
        one_way_matched_users = list(matches.values())

        user_fields = ["name", "curso", "age", "sex", "ice_breaker", "sexes", "top_1", "top_2", "top_3", "facebook",
                       "top_1_text", "top_2_text", "top_3_text", "top_1_item", "top_2_item", "top_3_item"]

        # list of dicts
        double_matches_list = list()
        exemplo = list()
        query_pessoa = dict()
        dados_double_match = dict()

        print(one_way_matched_users)

        for item in one_way_matched_users:
            if item != 0:
                person_query = Matches.query.filter_by(user_id=item).first()
                if person_query:
                    for i in range(0, 20):
                        key = "name_{}".format(i)
                        key = dict()
                        query_pessoa['match{}'.format(i+1)] = getattr(person_query, 'match{}'.format(i+1))
                        if query_pessoa['match{}'.format(i+1)] == user_id:
                            person_double_matched = User.query.filter_by(user_id=item).first()
                            for field in user_fields:
                                key[field] = getattr(person_double_matched, field)
                            double_matches_list.append(key)

        print(double_matches_list)

        if len(double_matches_list) == 0:
            message = "As pessoas ainda não tiveram a chance de ver seu perfil e se conectar com você. Espere por um " \
                      "tempo até que as pessoas tenham a chance de se conectar com você!"
        else:
            message = ""

        return render_template("matched.html", double_matches_list=double_matches_list, message=message)

# Log out function - copied from Problem Set 8
@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
