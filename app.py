from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    out = "<h2>Урааааа!</h2><br /><P>"
    out += str( time.time() )
    out += "</P>"
    return out

@app.route('/blog')
def blog():
    return "<h2>My blog.</h2>"

if __name__ == '__main__':
    app.run(debug=True)