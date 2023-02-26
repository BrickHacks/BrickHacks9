from flask import Flask, Response, render_template

from SignScanner import get_video_stream, getPrediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/translate')
def about_page():
    prediction = getPrediction()
    return render_template("translate.html", prediction = prediction)

@app.route('/video_feed')
def video_feed():
    return Response(get_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/levels')
def dashboard_page():
    return "levels"

if __name__ == '__main__':
    app.run()
