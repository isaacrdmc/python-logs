from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ? Inicializamos la SQLAlchemy para usarla más adelante en los modelos
db = SQLAlchemy()

# Creamos la app y configuramos algunos parámetros básicos
def create_app():
    app = Flask(__name__)

    # Configuración de para la Base de datos SQLite
    app.config['SECRET_KEY'] = 'root'   # 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'       # Nombre del archivo 

    # iniciamos la APP y conectamos la BD
    db.init_app(app)


    # ? Separamos los archivos de las rutas a utilizar por medio de 'Blueprints'
    
    # ^ aca iran las rutas que esten relacinadas con la autenticación: iniciar sesión o registrarse.
    from project.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # ^ Aca las rutas no relacionadas con autenticación: Página principal o cualquier otra funcionalidad de la app.
    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    
    return app



# * Retornamos la APP









# TODO 
'''
* En un terminal, puede configurar los valores FLASK_APP y FLASK_DEBUG:


````set FLASK_APP=project/__init__.py````    El nombre del poryecto, en nuestro caso 'proyect' es la carpeta donde esta todo el sistema
````set FLASK_DEBUG=1````        Le decimos que se ejecute en modo debug

# Despues lo ejecutamos
`````flask run`````


set FLASK_APP=project
set FLASK_DEBUG=1
flask run
'''







# from flask import Flask

# def create_app():
#     app = Flask(__name__)

#     @app.route('/')
#     def hello_world():
#         return '¡Hola, Mundo!'

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)
