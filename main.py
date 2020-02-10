from flask import Flask, render_template
app = Flask(__name__)
from validate_email import validate_email
@app.route("/")
def home():
    is_valid = validate_email("rjgopal769@gmail.com",verify=True)
    return is_valid
#     return render_template("home2.html")

@app.route("/about2")
def about():
    return render_template("about2.html")

@app.route("/ash")
def ash():
    return "Hello, Ash!"

if __name__ == "__main__":
    app.run(debug=True)
