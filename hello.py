from flask import Flask
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a </h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/user/<name>')
def user(name):
    return '<h1>hello %s!</hi>' %name

@app.route('/request')
def request():
    user_agent = request.headers.get('User-Agent')
    return '<p>your browser is %s</p>' %user_agent

@app.route('/redirect')
def go():
    return redirect('http://www.baidu.com')

@app.route('/users/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>hello, %s</h1>'%user.name
    

if __name__ == '__main__':
    app.run(debug=True)
