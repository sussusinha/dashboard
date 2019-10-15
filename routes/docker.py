
import logging

import flask
import docker

from services import decorators


blueprint = flask.Blueprint('docker', __name__)


@blueprint.route('/docker', methods=[ 'GET', 'POST' ])
@decorators.login_required
def docker_action():

    conn = None

    try:
        conn = docker.DockerClient('tcp://127.0.0.1:2376')
    except:
        return flask.jsonify({
            'mensagem': 'Erro de conexão com o Docker'
        }), 500
    
    context = {
        'containers': conn.containers.list(all=True)
    }
    
    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/<containerid>/start', methods=[ 'GET' ])
def start_container(containerid):

    conn = None

    try:
        conn = docker.DockerClient('tcp://127.0.0.1:2376')
    except:
        return flask.jsonify({
            'mensagem': 'Erro de conexão com o Docker'
        }), 500

    container = conn.containers.get(containerid)

    if container:
        container.start()
        flask.flash('Container {} iniciado'.format(containerid), 'success')
        logging.info('Container {} iniciado'.format(containerid))
        
    return flask.redirect('/docker')

@blueprint.route('/docker/<containerid>/stop', methods=[ 'GET' ])
def stop_container(containerid):

    conn = None

    try:
        conn = docker.DockerClient('tcp://127.0.0.1:2376')
    except:
        return flask.jsonify({
            'mensagem': 'Erro de conexão com o Docker'
        }), 500

    container = conn.containers.get(containerid)

    if container:
        container.stop()
        flask.flash('Container {} pausado'.format(containerid), 'warning')

    return flask.redirect('/docker')