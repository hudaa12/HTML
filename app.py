import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route('/hello')
def get_hello():
    return render_template("hello.html", message="Hello, world!")


@app.route('/goodbye')
def get_goodbye():
    return render_template("goodbye.html")





# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
