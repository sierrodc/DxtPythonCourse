# pip install Flask
# execute "flask run"

from flask import Flask, render_template

app = Flask(__name__)

# basic path reply-response
@app.route('/')
def home():
    return "Hello from flask"

# reply-response with parameters
@app.route('/hello/<name>')
def hello(name=None):
    return f"Hello {name} from flask"

# template response
@app.route('/helloTemplate/<name>')
def helloTmpl(name=None):
    return render_template("hello.html", name=name)

# error response
@app.errorhandler(404)
def page_not_found(error):
    return f"Page not found", 404