from flask import Flask

def create_app():
    app = Flask(__name__)

    #регистрация маршрутов
    from . import routes
    app.register_blueprint(routes.bp)

    return app