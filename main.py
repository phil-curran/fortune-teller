from flask import Flask, render_template, request


app = Flask(__name__)

redFortune = 'You will eat a potato with dinner, but it won\'t be very good.'
yellowFortune = 'You will shop for your favorite snack, only to discover it has been discontinued by the manufacturer.'
blueFortune = 'You will develop extreme flatulence before an important public speaking engagement.'
greenFortune = 'You will never win the lottery.'

oneFortune = 'your doctor will tell you to get more fiber in your diet.'
twoFortune = 'you will run out of toilet paper at the worst possible moment.'
threeFortune = 'you have an unnecessarily harsh opinion about brussel sprouts.'
fourFortune = 'your pet hamster would like to politely request that you stop singing in the shower.'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fortune", methods=["GET", "POST"])
def fortune():
    if request.method == "POST":
        username = request.form["user"]
        temp_color = request.form["color"]
        if temp_color == "red":
            favorite_color = redFortune
        elif temp_color == "yellow":
            favorite_color = yellowFortune
        elif temp_color == "blue":
            favorite_color = blueFortune
        elif temp_color == "green":
            favorite_color = greenFortune
        favorite_number = request.form["number"]
        if favorite_number == "1":
            favorite_number = oneFortune
        elif favorite_number == "2":
            favorite_number = twoFortune
        elif favorite_number == "3":
            favorite_number = threeFortune
        elif favorite_number == "4":
            favorite_number = fourFortune
        return render_template("fortune.html", username=username, favorite_color=favorite_color, favorite_number=favorite_number)
    return "Please submit the form first."


# Run the app
if __name__ == '__main__':
    app.run(debug=True)