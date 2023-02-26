import random
from flask import Flask, Response, render_template, request
import cv2
import ffmpeg
from SignScanner import get_video_stream, getPrediction
from twilio.rest import Client
# import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone

app = Flask(__name__)

@app.route('/')
def home():
    print('home')
    return render_template('home.html')


@app.route('/translate')
def translate_page():
    prediction = getPrediction()
    print("pred" + prediction)
    return render_template("translate.html", prediction = prediction)

@app.route('/video_feed')
def video_feed():
    print('videofeed')
    return Response(get_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/levels')
def dashboard_page():
    print('levels')
    return render_template("levels.html")

animals = {
	"A": "/css/letters/A.png",
	"B": "/css/letters/B.png",
	"C": "/css/letters/C.png",
    "D": "/css/letters/D.png",
    "E": "/css/letters/E.png",
    "F": "/css/letters/F.png",
    "G": "/css/letters/G.png",
    "H": "/css/letters/H.png",
    "I": "/css/letters/I.png",
    "J": "/css/letters/J.png",
    "K": "/css/letters/K.png",
    "L": "/css/letters/L.png",
    "M": "/css/letters/M.png",
    "N": "/css/letters/N.png",
    "O": "/css/letters/O.png",
    "P": "/css/letters/P.png",
    "Q": "/css/letters/Q.png",
    "R": "/css/letters/R.png",
    "S": "/css/letters/S.png",
    "T": "/css/letters/T.png",
    "U": "/css/letters/U.png",
    "V": "/css/letters/V.png",
    "W": "/css/letters/W.png",
    "X": "/css/letters/X.png",
    "Y": "/css/letters/Y.png",
    "Z": "/css/letters/z.png"
}

@app.route('/alphabet')
def index():
    print('here')
    # Get a random animal and its image filename
    animal, image_filename = random.choice(list(animals.items()))

    return render_template('alphabet.html', image_filename=image_filename, animal=animal)

@app.route('/guess', methods=['POST'])
def guess():
    # Get the guessed animal from the form
    guessed_animal = request.form['guess']

    # Get the actual animal from the form
    actual_animal = request.form['animal']

    if guessed_animal.lower() == actual_animal.lower():
        message = "Congratulations, you guessed it!"
    else:
        message = "Sorry, that's not the right answer. Try again!"

    # Get a new random animal and its image filename
    animal, image_filename = random.choice(list(animals.items()))

    return render_template('alphabet.html', image_filename=image_filename, animal=animal, message=message)



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
    
    
