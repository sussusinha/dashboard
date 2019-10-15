
import flask
import ldap3


blueprint = flask.Blueprint('auth', __name__)

LDAP_SERVER_URI = 'ldap://127.0.0.1:389'

OBJECT_CLASS = [
    'top',
    'person',
    'organizationalPerson',
    'inetOrgPerson',
    'posixAccount'
]

USERNAME = 'admin'
PASSWORD = '4linux'

def create_ldap_connection():
    try:
        conn = ldap3.Connection(
            ldap3.Server(LDAP_SERVER_URI),
            'cn={},dc=dexter,dc=com,dc=br'.format(USERNAME),
            PASSWORD
        )
        conn.bind()
        return conn
    except:
        return None

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def auth_action():

    conn = create_ldap_connection()

    if not conn:
        return flask.jsonify({
            'mensagem': 'Erro na conexão com LDAP'
        })
    
    if flask.request.method == 'POST':

        email = flask.request.form.get('email')
        password = flask.request.form.get('password')


        conn.search(
            'uid={},dc=dexter,dc=com,dc=br'.format(email),
            '(objectClass=person)',
            attributes=[
                'sn',
                'userPassword'
            ]
        )
        
        results = conn.entries

        if len(results) > 0:
            
            saved_password = results[0]['userPassword']
            saved_password = saved_password.value.decode()
            
            if password != saved_password:
                return flask.redirect('/sign-in')
                
            flask.session['authenticated'] = True
            return flask.redirect('/docker')

    context = {
        'route_is_public': True
    }
    return flask.render_template('sign-in.html', context=context)

@blueprint.route('/sign-up', methods=[ 'GET', 'POST' ])
def sign_up_action():

    conn = create_ldap_connection()

    if not conn:
        return flask.jsonify({
            'mensagem': 'Erro na conexão com LDAP'
        })
    
    if flask.request.method == 'POST':
        user = {
            'cn': flask.request.form.get('name'),
            'sn': flask.request.form.get('surname'),
            'mail': flask.request.form.get('email'),
            'uidNumber': id(flask.request.form),
            'gidNumber': 1,
            'uid': flask.request.form.get('email'),
            'homeDirectory': '/home/{}.{}'.format(
                flask.request.form.get('name'),
                flask.request.form.get('surname').split(' ', 1),
            ),
            'userPassword': flask.request.form.get('password'),
        }
        res = conn.add(
            'uid={},dc=dexter,dc=com,dc=br'.format(
                flask.request.form.get('email')
            ),
            OBJECT_CLASS,
            user
        )
        if res:
            return flask.redirect('/sign-in')
            
    context = {
        'route_is_public': True
    }

    return flask.render_template('sign-up.html', context=context)

@blueprint.route('/sign-out', methods=[ 'GET' ])
def sign_out_action():
    del flask.session['authenticated']
    return flask.redirect('/sign-in')
    