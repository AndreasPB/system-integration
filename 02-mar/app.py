from bottle import default_app, get, post, run, view

#######################################
@get("/")
@view("index")
def _():
    return


@post("/api-login")
def _():
    return "NO"


#######################################
try:
    # Server AWS | Production
    import production

    application = default_app()
except:
    # Localhost | Development
    print("Running dev")
    run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
