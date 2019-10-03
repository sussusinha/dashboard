
import flask


blueprint = flask.Blueprint('docker', __name__)

@blueprint.route('/docker', methods=[ 'GET', 'POST' ])
def docker_action():
    context = {

    }
    return flask.render_template('docker.html', context=context)

