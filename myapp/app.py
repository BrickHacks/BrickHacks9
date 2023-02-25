from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/templates/home.html')

@app.route('/about')
def about_page():
    return "about"

@app.route('/dashboard')
def dashboard_page():
    return "dashboard"

@app.route('/contact')
def contact_page():
    return "contact"

if __name__ == '__main__':
    app.run()
