from flask import Flask, render_template , request, redirect, url_for, flash, session
from datetime import datetime 

app = Flask(__name__)
app.config['SECRET_KEY']='secret_123'

usuarios = {
    'estrella@correo.com': {
        'password': 'estrella123',
        'nombre': 'estrellla'
    }
}

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

@app.route("/registrarse" , methods=["GET", "POST"])
def reg():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        password = request.form.get('password')

        if not nombre or not correo or not password:
            flash('Por favor, completa todos los campos.', 'warning')
            return redirect(url_for('registro'))

        if correo in usuarios:
            flash('Este correo ya fue registrado.', 'danger')
            return redirect(url_for('registro'))

    
        usuarios[correo] = {
            'nombre': nombre,
            'password': password
        }

        flash('Registro exitoso. Favor de iniciar sesion', 'success')
        return redirect(url_for('inicio'))

    return render_template('registro.html')

@app.route("/iniciar", methods=["GET", "POST"])
def iniciar():

    if request.method == 'POST':
        correo = request.form.get('Correo_electronico', '').strip()
        
        password = request.form.get('Contrasena', '')

        usuario = usuarios.get(correo)

        if usuario and usuario['password'] == password:
            session['usuario'] = usuario['nombre']
            flash(f"Bienvenido, {usuario['nombre']}!", "success")
            return redirect(url_for('inicio'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')
            return redirect(url_for('iniciar'))
    

    return render_template('iniciar.html')


@app.route('/cerrar')
def cerrar():
    session.clear()
    flash("Has cerrado sesión.", "info")
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)
