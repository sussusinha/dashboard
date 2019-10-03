
import flask


blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def auth_action():
    context = {

    }
    return flask.render_template('sign-in.html', context=context)