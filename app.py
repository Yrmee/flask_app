import datetime
from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", utc_dt=datetime.datetime.now().strftime("%d %B %Y %H:%M"))

@app.route("/<page_name>")
def other_page(page_name): 
    response = make_response(render_template("404.html", page_name=page_name), 404)
    return response

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", debug=True)
