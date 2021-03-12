from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from api.account.AccountAPI import account_api
from api.algorithms.algorithmsAPI import algo_api

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask App"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)



app.register_blueprint(account_api)
app.register_blueprint(algo_api)

@app.route("/")
def hello():
    return "Hello World! Welcome to the"

if __name__ == "__main__":
    app.run()

# for nodemon kind of functionality in flask run the following commands
# export FLASK_APP=app.py
# export FLASK_ENV=development 
# yash@yash-Inspiron-5558:~/Desktop/Python/flaskApi$ flask run
# export FLASK_DEBUG=1 ---- for nodemon 
# 