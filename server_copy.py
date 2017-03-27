from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def presentation_page():
    return render_template("graduation.html")

if __name__ == "__main__":
    app.run(debug=True)