from bottle import run, template, get, post, request, debug
# http://localhost:8060/ --> anything after is the route

@get("/")
def get_index():
    return ("Hello!")


def get_hello():
    return ("Hello!!! :)")

@get("/hello")
@get("/hello/<name>")
def get_hello(name="World"):
    return template("hello.tpl", name="bob", extra=None)

@get("/greet")
@get("/greet/<name>")
def get_greet(name="World"):
    return template("hello.tpl", name="bob", extra="Happy Birthday")


@get("/greeting/<names>")
def get_greeting(names):
    names = names.split(',')
    return template("greetings.tpl", names=names)


@get("/login")
def get_login():
    return template("login", message="")

@post("/login")
def post_login():
    username = request.forms["username"]
    password = request.forms["password"]
    if password != "magic":
            return template("login", message="Bad Password")
    return template("hello", name=username+"!!!", extra="Happy Birthday")

debug(True)
run(host="localhost", port=8060, reloader=True)

