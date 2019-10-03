
import flask


blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET', 'POST' ])
def gitlab_action():
    context = {

    }
    return flask.render_template('gitlab.html', context=context)