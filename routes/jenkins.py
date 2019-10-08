
import flask
import jenkins


blueprint = flask.Blueprint('jenkins', __name__)

opts = {
    'url': 'http://localhost:8080/',
    'username': 'admin',
    'password': '4linux'
}

err = {
    'mensagem': 'Falha na conexão com o Jenkins'
}

@blueprint.route('/jenkins', methods=[ 'GET', 'POST' ])
def jenkins_action():

    conn = None

    try:
        conn = jenkins.Jenkins(**opts)
    except:
        return flask.jsonify(err, 500)

    jobs = [
        conn.get_job_info(j['fullname']) for j in conn.get_jobs()
    ]

    context = {
        'jobs': jobs
    }
    
    return flask.render_template('jenkins.html', context=context)

@blueprint.route('/jenkins/build/<jobid>', methods=[ 'GET', 'POST' ])
def jenkins_job_action(jobid):

    conn = None

    try:
        conn = jenkins.Jenkins(**opts)
    except:
        return flask.jsonify(err, 500)
    
    if flask.request.method == 'POST':
        config = flask.request.form.get('config') or jenkins.EMPTY_CONFIG_XML
        conn.reconfig_job(jobid, config.strip())
        
    context = {
        'job': {
            'name': jobid,
            'config': conn.get_job_config(jobid)
        }
    }

    return flask.render_template('jenkins-job.html', context=context)

