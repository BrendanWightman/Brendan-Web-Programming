from bottle import redirect, run, template, get, post, request, debug, response
# http://localhost:8060/ --> anything after is the route

########

import os
import json
import random
import string

def new_user(username):
    user = {
        "username" : username
    }
    os.makedirs("data/users", exist_ok=True)
    session_file = f"data/users/{username}.user" 
    with open(session_file, 'w') as f:
        json.dump(user, f)
    return user

def load_user(username):
    try:
        os.makedirs("data/users", exist_ok=True)
        session_file = f"data/users/{username}.session"
        with open(session_file, 'r') as f:
            user = json.load(f)
        
    except Exception as e:
        print("user error: ", e)
        user = new_user()
    return user


def save_user(user):
    os.makedirs("sessionFile", exist_ok=True)
    username = user['username']
    session_file = f"data/usuers/{username}.user"
    with open(session_file, 'w') as f:
        json.dump(username, f)
    print("Save user is: ", user)


def random_id():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=16))

def load_session(request, username=''):
    os.makedirs("data/sessionFile", exist_ok=True)
    session_id = request.get_cookie('session_id', default=None)
    try:
        if session_id == None:
            raise Exception("No sesion id cookies found")  
        session_file = f"data/sessionFile/{session_id}.session"
        with open(session_file, 'r') as f:
           session = json.load(f)
        
        
    except Exception as e:
        print(e)
        session_id = random_id()
        session = {
            'session_id': session_id
        }
        session_file = f"data/sessionFile/{session_id}.session"
        if username in session:
            session['user'] = load_user(username)
        else:
            session['user'] = {}
        with open(session_file, 'w') as f:
            json.dump(session, f)
    response.set_cookie("session_id", session_id)        

    return session


def save_session(session, response):
    os.makedirs("sessionFile", exist_ok=True)
    session_id = session['session_id']
    if 'user' in session:
        save_user(session['user'])
    session_file = f"data/sessionFile/{session_id}.session"
    with open(session_file, 'w') as f:
        json.dump(session, f)
    response.set_cookie("session_id", session_id)

    return session


########

@get("/")
@get("/hello")
def get_hello(name=None):
    session = load_session(request)
    if 'username' in session:
        name = session['username']
    else:
        name = "stranger"
    favcolor = session.get('favcolor', 'not known')
    save_session(session, response)
    return template("hello.tpl", name=session['username'], color=favcolor)


@get("/login")
def get_login():
    session = load_session(request)
    save_session(session, response)
    return template("login")

@post("/login")
def post_login():
    session = load_session(request)
    
    username = request.forms["username"]
    password = request.forms["password"]
    favcolor = request.forms["favcolor"]
    #if password != "magic":
    #   session_id=request("session_id", default="asdawegerg")
    #   save_session(session, response)
    #    redirect("/login")
    #   return template("login", message="Bad Password")
    session['username'] = username
    session['user'] = load_user(username)
    session['user']['favcolor'] = favcolor
    session['favcolor'] = favcolor
    save_session(session, response)
    redirect("/hello")

debug(True)
run(host="localhost", port=8060, reloader=True)

