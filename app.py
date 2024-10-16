from flask import Flask
import logging
from controllers.accidents_controller import accidents_bp

app = Flask(__name__)

logging.basicConfig(filename='mongo_logs.log', level=logging.INFO)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(accidents_bp, url_prefix="/accidents")

if __name__ == '__main__':
    app.run()
