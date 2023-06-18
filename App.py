from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySQL connection
app.config['MYSQL_HOST'] = '34.224.103.212'
app.config['MYSQL_USER'] = 'support'
app.config['MYSQL_PASSWORD'] = 'sistemas20.'
app.config['MYSQL_DB'] = 'ccities_data'
mysql = MySQL(app)

#secret clave
app.secret_key = 'HOLLM'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/iniciar_sesion')
def inicia_sesion():
    return render_template('inicia_sesion.html')

@app.route('/add_usuarios1', methods=['POST'])
def add_usuarios1():
    if request.method == 'POST': #Define método de envío
        nombre = request.form['nombres'] # request.form recoge datos de formulario
        correo = request.form['correo']
        contrasenia = request.form['contrasenia']
        genero = request.form['genero']
        nacimiento = request.form['nacimiento']
        
        cur = mysql.connection.cursor() #genera conexion DB SQL
        cur.execute('INSERT INTO usuario_vecinos (nombre, correo, contrasenia, genero, nacimiento) VALUES (%s,%s,%s,%s,%s)', 
        (nombre, correo, contrasenia, genero, nacimiento)) # ejecuta comando SLQ datos recogidos del form
        mysql.connection.commit() # Guarda cambios en DB
        flash('Client Added Succesfully')
        return redirect(url_for('home')) #Redirecciona a pagina Index
    #return render_template('registro.html')

@app.route('/add_usuarios2')
def add_usuarios2():
    return render_template('registroIng.html')


if __name__=='__main__':
    app.run(port=5000, debug = True)