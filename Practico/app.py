from datetime import datetime
from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import preceptor, curso, estudiante, asistencia

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/iniciar_sesion',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        print("",request.form['correo'])
        if request.form.get('rol') == 'preceptor':
            preceptor1= preceptor.query.filter_by(correo=request.form['correo']).first()
            print("",request.form['correo'])
            if preceptor1 is None:
                return render_template('error.html', error="El correo del preceptor no existe...")
            else:
                validar = preceptor1.clave == request.form['password']
                if (validar):           
                    return render_template('registrar.html')
                else:
                    return render_template('error.html', error="Los datos ingresados no son correctos...")
        else:
            return render_template('error.html', error="El rol no es correcto...")
    else:
        return render_template('sesion.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)