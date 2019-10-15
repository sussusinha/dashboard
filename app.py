
import os
import sys
import logging

import flask

from routes.docker import blueprint as docker
from routes.jenkins import blueprint as jenkins
from routes.gitlab import blueprint as gitlab
from routes.auth import blueprint as auth


logging.basicConfig(
    filename='app.log',
    level=logging.WARNING,
    format='%(asctime)s [ %(levelname)s ] %(name)s ' +
        '[ %(funcName)s ] [ %(filename)s, %(lineno)s ] %(message)s',
    datefmt='[ %d/%m/%Y %H:%M:%S ]'
)

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(docker)
app.register_blueprint(jenkins)
app.register_blueprint(gitlab)
app.register_blueprint(auth)

logging.debug('Iniciando a aplicação ...')

@app.errorhandler(404)
def handle_404(err):
    return flask.render_template('404.html')

@app.route('/', methods=[ 'GET' ])
def get_home():
    return flask.redirect('/docker')

if __name__ == "__main__":
    app.run(host='0.0.0.0')