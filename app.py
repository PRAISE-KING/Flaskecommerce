# client-server
# Framework
# Flask
# request-response

# A client - computer that that sends requests to the server ,listens to server response (webbrowser)
# server - process clients request, sends response to the client  (flask application.)

# Framework - make development easy by utilizing the reusable code....e.g flask,django

from flask import *

# start
app = Flask(__name__)

# decorators (@)
# flask routing
# method - route()
# to bind the method route to our app object, then we use decorator @

@app.route('/home')
def home_page():
    return "Hello Welcome to flask"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')


@app.route('/')
def index():
    return "View index page here!"

# ''' ''' -for multi-statement

@app.route('/add')
def add():
    fruits = ['mango' , 'orange']
    return fruits

# how to load css,js,images,bootstrap on flask
# static folder - stores all the above

@app.route('/back')
def back():
    return render_template('background.html')

app.run(debug=True)
# end