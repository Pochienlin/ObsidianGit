# Flask
UID: 202204181156
Tags: #🌲 
Links: [[Enterprise Solution]] [[Enterprise Solution Development]] [[web applications]] [[Web app development]]

## Overview
```ad-abstract
title: What is Flask?

Flask is a minimal python app wrapper module. By using Flask, we can turn our Python scripts into simple micro-apps that can be called while running
```

## A Minimal Application

A minimal Flask application looks something like this:

from flask import Flask

```python
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
#### So what did that code do?
1.  First we imported the [`Flask`](https://flask.palletsprojects.com/en/2.1.x/api/#flask.Flask "flask.Flask") class. An instance of this class will be our WSGI application.
2.  Next we create an instance of this class. The first argument is the name of the application’s module or package. `__name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
3.  We then use the [`route()`](https://flask.palletsprojects.com/en/2.1.x/api/#flask.Flask.route "flask.Flask.route") decorator to tell Flask what URL should trigger our function.
4.  The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

Save it as `hello.py` or something similar. Make sure to not call your application `flask.py` because this would conflict with Flask itself.

To run the application, use the **flask** command or **python -m flask**. Before you can do that you need to tell your terminal the application to work with by exporting the `FLASK_APP` environment variable:

---
`$ export FLASK_APP=hello
`$ flask run
```
* Running on http://127.0.0.1:5000/`
```
---

## Routing
You can wrap an app using [[HTTP Methods]], most likely POST, PUT or GET, rarely but possibly DELETE

#### Preparing a wrapper
Ensure that flask, or a flask base image (for [[Docker]]) is installed within the environment.

Import the Flask module on your app's script like so:
```python
from flask import Flask, redirect, url_for, request  
app = Flask(__name__)
```
Add this to the end of the script to ensure that debug mode is on (so that we can see what is happening whenever the app is called)
```python
if __name__ == '__main__':  
   app.run(port=5000, debug = True)
```
- `port` is up for the user to change. This is an optional argument. The default port for a Flask app is 5000

#### Wrapping a GET path

#### Wrapping with the POST/ PUT method
Example of a POST method path.
```ad-tip
title: Notice the difference
With the POST method, you can still pass a variable via the path. This simplifies variable passing.
Alternatively, you can use the `request` module to find the POST variable via `request.args()` or `request.json()` depending on the data type
```

###### Example 1: passing variable via url
```python 
@app.route("/book/<string:isbn13>", methods=['POST'])
def create_book(isbn13): 
    if (Book.query.filter_by(isbn13=isbn13).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "isbn13": isbn13
                },
                "message": "Book already exists."
            }
        ), 400
 
    data = request.get_json()
    book = Book(isbn13, **data)
 
    try:
        db.session.add(book)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "isbn13": isbn13
                },
                "message": "An error occurred creating the book."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": book.json()
        }
    ), 201
```

###### Example 2: Passing variables via Request module with both POST and GET
```python
@app.route('/login',methods = ['POST', 'GET'])  
def login():  
   if request.method == 'POST':  
      user = request.form['nm']  
      return redirect(url_for('success',name = user))  
   else:  
      user = request.args.get('nm')  
      return redirect(url_for('success',name = user))
```

## Running the application 
To run the application on localhost (127.0.0.1/\<PORT\>), use the command line, or turn it into a docker image using a Dockerfile and running a container from that.
```cmd
$ cd <path to my app>

$ python3 myapp.py
```

Assuming the app is running on port 5000, the console will log the following debug messages (recall that at the end of the app we enabled the debugger with `debug=true`)

```console
* Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

if instead the debugger is not enabled (`debug=false`)

```console
export FLASK_DEBUG=false

 * Environment: development
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
