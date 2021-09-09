from bottle import route, run, template

# http://localhost:8060/ --> anything after is the route

@route("/")
def get_index():
    return ("Hello!")


def get_hello():
    return ("Hello!!! :)")

@route("/hello")
@route("/hello/<name>")
def get_hello(name="World"):
    return template("hello.tpl", name="bob", extra=None)

@route("/greet")
@route("/greet/<name>")
def get_greet(name="World"):
    return template("hello.tpl", name="bob", extra="Happy Birthday")


@route("/greeting/<names>")
def get_greeting(names):
    names = names.split(',')
    return template("greetings.tpl", names=names)

run(host="localhost", port=8060)

