from bottle import default_app, route, run,template

@route('/')
def hello_world():
    return "Hello World"

@route('/hello/<name>')
def hello_2world(name):
    return template("goodbye", name=name) 

run(host="localhost", port=(8090))