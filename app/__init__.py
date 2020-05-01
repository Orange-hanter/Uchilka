from flask import Flask, url_for, render_template
from flask import request
import csv
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        try:
            print(request.form['inputEmail'], request.form['inputPassword'])
            if valid_login(request.form['inputEmail'], request.form['inputPassword']):
                return log_the_user_in(request.form['inputEmail'])
            else:
                error = 'Invalid username/password'
        except KeyError:
            error = "PIZDEC NAHUI BLIAT"
            return render_template('logIn.html', error=error)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('logIn.html', error=error)


def valid_login(login, pas):
    file = request.files['./static/users.csv']
    #TODO: Learn how to get acces to file whith requesst
    with open('./static/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print(row)
    return True


def log_the_user_in(gg):
    return render_template('index.html')


with app.test_request_context():
    pass