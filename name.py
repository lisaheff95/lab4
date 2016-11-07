from flask import Flask
app = Flask(__name__)

@app.route("/name/<Lisa>")
def name(Lisa):
    return "My name is " + Lisa

if __name__ == "__main__":
    app.run()
