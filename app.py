from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Flask is a micro web framework for Python
# It is lightweight and easy to use for building web applications

tasks = []
feedback = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)

@app.route('/about')
def about():
    return render_template('about.html' ,name="Daniel" ,passion="Web Development")

@app.route('/greet', methods = ['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('user.html', username=name)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)