from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sistemas20.'
app.config['MYSQL_DB'] = 'CCitiesData'
mysql = MySQL(app)

#secret clave
app.secret_key = 'HOLLM'

@app.route('/')
def home():
    return "Holaaa"

@app.route('/add_usuarios1')
def add_usuarios1():
    """if request.method == 'POST': #Define método de envío
        nombre = request.form['nombre'] # request.form recoge datos de formulario
        correo = request.form['correo']
        contrasenia = request.form['contrasenia']
        genero = request.form['genero']
        nacimiento = request.form['nacimiento']
        
        cur = mysql.connection.cursor() #genera conexion DB SQL
        cur.execute('INSERT INTO usuarios_vecinos (nombre, correo, contrasenia,genero, nacimiento) VALUES (%s, %s, %s,%s,%s)', 
        (nombre, correo, contrasenia,genero, nacimiento)) # ejecuta comando SLQ datos recogidos del form
        mysql.connection.commit() # Guarda cambios en DB
        flash('Usuario registrado')
        return redirect(url_for('add_usuario1'))"""
    return render_template('registro.html')

@app.route('/add_usuarios2')
def add_usuarios2():
    return render_template('registroIng.html')


if __name__=='__main__':
    app.run(port=3000, debug = True)