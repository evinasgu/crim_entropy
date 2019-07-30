from flask import Flask
from flask import Blueprint
from flask_restful import Api
from criminal_danger.resource import StreetResource, CriminalDangerResource


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    api_blueprint = Blueprint('api', __name__)
    api = Api(api_blueprint)

    api.add_resource(StreetResource, 'street', endpoint='streets')
    api.add_resource(CriminalDangerResource, 'criminal_danger', endpoint='criminal_danger_report')

    app.register_blueprint(api_blueprint, url_prefix='/api/v1/')

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
