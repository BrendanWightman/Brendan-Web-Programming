import random
from bottle import run, template, get, post, request, debug, response

# http://localhost:8060/ --> anything after is the route

#session management\
session = {}

def new_session():
    sessionId =  str(random.randint(100000, 999999))
    session[sessionId] = {
        "username" : "world"
    }

def get_session(sessionId):
    if sessionId in session:
        return session[sessionId]
    return None


@get("/")
def get_index():
    return ("Hello!")


def get_hello():
    return ("Hello!!! :)")

@get("/hello")
def get_hello():
    sessionId = request.get_cookie("sessionId", default=new_session())
    session = get_session(sessionId)
    print(session)
    uername = session["username"]

    response.set_cookie("sessionId", sessionId)
    return template("hello.tpl", name=sessionId, extra=None)

@get("/login")
def get_login():
    sessionId = request.get_cookie("sessionId", default=new_session())
    session = get_session(sessionId)
    print(session)
    response.set_cookie("sessionId", sessionId)
    return template("login", message="")

@post("/login")
def post_login():
    sessionId = request.get_cookie("sessionId", default=new_session())
    session = get_session(sessionId)
    print(session)

    username = request.forms["username"]
    password = request.forms["password"]
    if password != "magic":
            return template("login", message="Bad Password")
    
    
    session['username'] = username
    response.set_cookie("sessionId", sessionId)
    return template("hello", name="session " + sessionId+"!!!", extra="Happy Birthday")

debug(True)
run(host="localhost", port=8060, reloader=True)

