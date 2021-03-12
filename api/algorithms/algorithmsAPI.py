from flask import Blueprint

algo_api = Blueprint('algorithms_api', __name__)

@algo_api.route("/algo")
def algorithms():
    return "list of algorithms"