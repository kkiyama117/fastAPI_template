import firebase_admin

from portfolio_api import utils, db


def initialize():
    init_firebase(_get_api_key())
    init_database()


def _get_api_key():
    api_key_path = utils.get_path("api.json")
    return api_key_path


def init_firebase(api_key_path):
    # maybe called multiple if debug or reload=True
    if not firebase_admin._apps:
        cert = firebase_admin.credentials.Certificate(str(api_key_path))
        firebase_admin.initialize_app(cert)


def init_database():
    # create database and insert schema
    db.SchemaBase.metadata.create_all(db.engine)
