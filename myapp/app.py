from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/translate')
def about_page():
    return render_template("translate.html")

@app.route('/levels')
def dashboard_page():
    return "levels"

if __name__ == '__main__':
    app.run()
