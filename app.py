from flask import Flask
import time

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<img src="/home/korvin/PycharmProjects/My_site_2/pic_trulli.jpg" alt="Trulli" width="500" height="333">'

@app.route('/')
def index():
     out = "<!DOCTYPE html>" \
           "<html>" \
           "<body style=\"background-color:powderblue;\">" \
           "<h1>Мій перший сайт!</h1>" \
           "<p>Тут буде текст...</p>" \
           "<p>Тут теж буде текст...</p>"\
           "</body>" \
           "</html>" \
           "<br /><P>"
     out += str( time.time() )
     out += "</P>"
     return out

@app.route('/blog')
def blog():
    return "<h2>My blog.</h2>"



if __name__ == '__main__':
    app.run(debug=True)