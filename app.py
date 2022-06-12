from flask import Flask, render_template, request,jsonify


app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return "Starting ML Project"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
	#app.run(debug=True)