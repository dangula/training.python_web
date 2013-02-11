

from bottle import Bottle, run,ResourceManager,template,request,redirect,url,error,abort,hook,route
from jinja2 import Environment, FileSystemLoader
jinja2_env = Environment(loader=FileSystemLoader('templates/'))
from bottle.ext import sqlite

plugin = sqlite.Plugin(dbfile='/tmp/bottle.db')
res = ResourceManager()
app = Bottle(__name__)
app.install(plugin)

import beaker.middleware

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

app_sesion = beaker.middleware.SessionMiddleware(app, session_opts)


@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']


def write_entry(title, text,db):
    db.execute('insert into entries (title, text) values (?, ?)',
                 [title, text])
    db.commit()


def get_all_entries(db):
    cur = db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return entries


@app.route('/')
def show_entries(db):
    entries = get_all_entries(db)
    jinja2_env.get_te
    template = jinja2_env.get_template('show_entries.html')
    return template.render( entries=entries)


def do_login(usr, pwd):
    if usr != 'admin':
        raise ValueError
    elif pwd != 'default':
        raise ValueError
    else:
        request.session['logged_in'] = True


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            do_login(request.form['username'],
                     request.form['password'])
        except ValueError:
            error = "Invalid Login"
        else:
            return redirect(app.url('show_entries'))
    template = jinja2_env.get_template('login.html')
    return template.render('login.html', error=error)


@app.route('/logout')
def logout():
    request.session.pop('logged_in', None)
    return redirect(app.url('show_entries'))


@app.route('/add', methods=['POST'])
def add_entry(db):
    if not request.session.get('logged_in'):
        abort(401)
        write_entry(request.form['title'], request.form['text'],db)
    return redirect(app.url('show_entries'))

if __name__ =='__main__':
    run(app=app_sesion,host='localhost', port=8080, debug=True)