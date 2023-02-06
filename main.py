from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fortune", methods=["GET", "POST"])
def fortune():
    if request.method == "POST":
        username = request.form["user"]
        favorite_color = request.form["color"]
        favorite_number = request.form["number"]
        return render_template("fortune.html", username=username, favorite_color=favorite_color, favorite_number=favorite_number)
    return "Please submit the form first."


# Run the app
if __name__ == '__main__':
    app.run(debug=True)