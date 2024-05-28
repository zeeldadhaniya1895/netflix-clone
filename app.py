from flask import Flask, render_template
app = Flask(__name__)


# Define the home page route
@app.route("/")
def hello():
    return render_template("netflix.html")

if __name__ == "__main__":
    app.run(debug=True)