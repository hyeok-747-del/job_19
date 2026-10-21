from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    data = "19기 어플리케이션 과정"
    return render_template("search.html", data=data)



if __name__ == "__main__":
    app.run(debug=True)


