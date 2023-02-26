from flask import Flask, render_template, Response
from SignScanner import get_video_stream, getPrediction
from twilio.rest import Client
# import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone

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

def sendMessage():
    # this is for hiding auth token
    # credFile = open('Credentials.json')
    # credData = json.load(credFile)
    # account_sid = credData["TWILIO_ACCOUNT_SID"]
    # auth_token = credData["TWILIO_AUTH_TOKEN"]
    account_sid = "AC624aa574738643549e12a2df76316c20"
    auth_token = "01b3bace253490520646718727eba8a9"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                from_='+18449514658',
                                body='You got this! Complete your daily ASL practice!',
                                to='+15085587876'
                            )
    print(message.sid)



scheduler = BackgroundScheduler(timezone=timezone('US/Eastern'))
scheduler.add_job(func=sendMessage, trigger=CronTrigger(hour=9, minute=0))
scheduler.start()


if __name__ == '__main__':
    app.run()
    
    
