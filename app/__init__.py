from flask import Flask

# Create the app
app = Flask(__name__)


# -------------------------------------------------------
# Home page route
@app.get("/")
def hello():
    return "<h1>Hello, World!</h1>"


# -------------------------------------------------------
# Test route
@app.get("/test")
def about():
    return "<h1>Testing... 1, 2, 3</h1>"

