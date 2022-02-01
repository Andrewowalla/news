from flask import Flask 
from config import config_options

bootsratp = Bootstrap()

def create_app('config_name'):
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app import views
    return app