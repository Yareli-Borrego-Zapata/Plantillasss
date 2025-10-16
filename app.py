from flask import Flask, render_template   

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/base")
def menu():
    return render_template("base.html")

@app.route("/animales")
def ani():
    return render_template("animales.html")

@app.route("/vehiculos")
def vei():
    return render_template("vehiculos.html")

@app.route("/maravillas")
def mun():
    return render_template("maravillas.html")

@app.route("/acerca")
def ace():
    return render_template("acerca.html")

@app.route("/registrarse")
def reg():
    return render_template("registrarse.html")

if __name__ == "__main__":
    app.run(debug=True)
