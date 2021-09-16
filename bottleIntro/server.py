from bottle import route, run

# http://localhost:8060/ --> anything after is the route

@route("/")
def get_index():
    return ("Hello!")


def get_hello():
    return ("Hello!!! :)")

@route("/hello")
@route("/hello/<name>")
def get_hello(name="World"):
    return (f"Hello, {name}")


run(host="localhost", port=8060)

