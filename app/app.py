from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from mysql_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:p%40ssw0rd1@mysqldb/test_mysql?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def inex():
    return 'Response Data'

@app.route('/another')
def fla():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/x_request/<user>')
def x_request(user):
    return f'x_request:{user}'

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exe_html')
def exe_html():
    return render_template('exercise.html')

@app.route('/exercise')
def my_html():
    s = request.args.get("my_name")
    return s

@app.route('/try_rest', methods=['POST'])
def try_rest():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)

@app.route('/try_html')
def try_html():
    return render_template('try_html.html')

@app.route('/show_data', methods=["GET", "POST"])
def show_data():
    return request.form

@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)
