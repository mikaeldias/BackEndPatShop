from flask import Blueprint

fornecedores_bp = Blueprint('fornecedores', __name__, template_folder='../templates/fornecedores')

# Importa as rotas para que elas sejam registradas no blueprint
from . import routes