from flask import Blueprint
# from . import db

# ? Definimos el BluePrint para las rutas de autenticación

# * Asiganmos una variable cuyo valor es la modulización de las rutas
# Nombre del Blueprint
# Nombre del módulo que define el Blueprint
auth = Blueprint('auth', __name__)



# ^ Rutas para el login
# ^ Usamos el decorador que indica para que sección del sistema es

# * Inicio de sesión
@auth.route('/login')
def login():
    return 'Login'

# * Registro del usuario
@auth.route('/signup')
def signup():
    return 'Signup'

# * Ruta para cerrar la sesión
@auth.route('/logout')
def logout():
    return 'Logout'