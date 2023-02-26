from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of animals and their corresponding image filenames
animals = {
	"Elephant": "/static/css/letters/A.png",
	"Giraffe": "/static/css/letters/B.png",
	"Lion": "/static/css/letters/C.png"
}

@app.route('/alphabet')
def index():
    print('here')
    # Get a random animal and its image filename
    animal, image_filename = random.choice(list(animals.items()))

    return render_template('/templates/alphabet.html', image_filename=image_filename, animal=animal)

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

    return render_template('/templates/alphabet.html', image_filename=image_filename, animal=animal, message=message)

if __name__ == '__main__':
    app.run(debug=True)
