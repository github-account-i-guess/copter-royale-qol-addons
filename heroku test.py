from flask import Flask
app = Flask(__name__)
@app.route("/")
def page():
    return "e <h1>Hello<h1> <h2> hello <h2>"
if __name__ == "__main__":
    app.run()