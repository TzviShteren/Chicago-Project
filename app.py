from flask import Flask
import logging
app = Flask(__name__)

logging.basicConfig(filename='mongo_logs.log', level=logging.INFO)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
    

# def parse_date(date_str: str):
#     has_seconds = len(date_str.split(' ')) > 2
#     return datetime.strptime(date_str, date_format)
#     date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'

#app.register_blueprint(cars_bp, url_prefix="/post")

if __name__ == '__main__':
    app.run()
