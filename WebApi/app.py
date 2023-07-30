
from flask import Flask
from flask import request
app =Flask(__name__)

@app.route("/")
def hello_word():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_word1")
def hello_word1():
    return "<h1>Hello, World1!</h1>"

@app.route("/hello_word2")
def hello_word2():
    return "<h1>Hello, World2!</h1>"

@app.route("/test")
def test():
    a=45+45
    return ("prashant a+b = {}".format(a))

@app.route("/test1")
def test1():
    data =request.args.get("x")
    return ("This is data form url = {}".format(data))

if __name__=="__main__":
    app.run(host="0.0.0.0")    