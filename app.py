from flask import Flask
import time

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<img src="/home/korvin/PycharmProjects/My_site_2/pic_trulli.jpg" alt="Trulli" width="500" height="333">'

@app.route('/')
def index():
    out = '<!DOCTYPE html><html><head><meta charset="utf-8">' \
          '<meta name="viewport" content="width=device-width, initial-scale=1"><title>Hello Bulma!</title>' \
          '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css">' \
          '<script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script></head><body>' \
          '<section class="section"><div class="container"><h1 class="title">'
    out += 'Hello guest</h1><p class="button is-primary">'
    out += str( time.time() )
    out += "</p></div></section></body></html>"
    return out

@app.route('/blog')
def blog():
    return "<h2>My blog.</h2>"



if __name__ == '__main__':
    app.run(debug=True)