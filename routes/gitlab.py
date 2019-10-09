
import flask
import requests


ACCESS_TOKEN = '9n4vGRsyoSy8kTuBKLxz'

USERS_API = 'http://localhost:8000/api/v4/users'
PROJECTS_API = 'http://localhost:8000/api/v4/projects'

blueprint = flask.Blueprint('gitlab', __name__)

def get(uri):
    return requests.get(uri, headers={
        'PRIVATE-TOKEN': ACCESS_TOKEN
    })

def get_users():
    res = get(USERS_API)
    if res.status_code == 200:
        return res.json()
    return []

def get_projects():
    res = get(PROJECTS_API)
    if res.status_code == 200:
        return res.json()
    return []

@blueprint.route('/gitlab', methods=[ 'GET', 'POST' ])
def gitlab_action():
    context = {
        'users': get_users(),
        'projects': get_projects()
    }
    return flask.render_template('gitlab.html', context=context)