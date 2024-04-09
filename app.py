from flask import Flask

app=Flask(__name__)

@app.route("/")

def iniciar():
    return "<h1>olá mundo!</h1>"

@app.route("/<idioma>")
def hello(idioma):
    if idioma=="portugues":
        mens="olá mundo!"

    elif idioma=="ingles":
        mens="Hello world!"


    return f'<h1>{mens}</h1>'