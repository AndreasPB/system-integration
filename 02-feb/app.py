from bottle import route, run, template, error, get


@error(404)
def _(error):
    return f"Woops! {error}"


@route("/hello/<name>")
def hello_name(name):
    return template("<b>Hello {{name}}</b>!", name=name)


@get("/")
def index():
    return "Welcome to the index page!"


run(host="127.0.0.1", port=1337, debug=True, reloader=True)
