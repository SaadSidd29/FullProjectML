from flask import Flask, render_template, request, jsonify
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])  # route to display the home page
def index():
    try:
        raise Exception("We are trying custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "CI CD Pipeline"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
	#app.run(debug=True)