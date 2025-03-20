from flask import Blueprint
# from . import bd


# ? Definimos el BluePrint para las rutas que no sean de autenticación

# * Asiganmos una variable cuyo valor es la modulización de las rutas
# Nombre del Blueprint
# Nombre del módulo que deine el Blueprint
main = Blueprint('main', __name__)


# ^ Rutas para el resto del sistema
# ^ Usamos el decorador que indica para que sección del sistema es


@main.route('/')
def index():
    return 'Index'

@main.route('/profile')
def profile():
    return 'Profile'