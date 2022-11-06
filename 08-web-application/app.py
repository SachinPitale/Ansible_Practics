from flask import Flask
import os

app=Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return " I am good, what about you"

if __name__=="__main__":
    app.run(port=5000)
