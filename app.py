from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config # Classe de configuração

# Inicializa SQLAlchemy(ORM)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Carrega Configurações do arquivo config.py(Referente ao BD)
    app.config.from_object(Config)

    #Inicializa o db (Associando com o Flask)
    db.init_app(app)

    # Importa e registra o blueprint de fornecedores
    from fornecedores.routes import fornecedores_bp  
    app.register_blueprint(fornecedores_bp, url_prefix='/fornecedores') # Tudo referente ao blueprint, na rota, deverá ter o /suppliers/

    with app.app_context():
        # Cria as tabelas no Banco de Dados. se elas não existirem
        db.create_all() 

    return app

