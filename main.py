from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


if __name__=='__main__':

    app.config.from_object(__name__)
    app.config['SECRET_KEY'] = 'qnaqnavkdn'
    app.run('0.0.0.0',port=80, debug=True)