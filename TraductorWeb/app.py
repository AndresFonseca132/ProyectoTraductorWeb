from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('registro.html')

@app.route('/reset_password')
def rpassword():
    return render_template('recuperar_contras.html')

if __name__ == '__main__':
    app.run(debug=True, port=2502)
