from flask import Flask 

def create_app() :

    app = Flask(__name__)

    from menu import views
    app.register_blueprint(views.menu, url_prefix="/menu")
    
    return app