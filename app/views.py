from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm, EditForm
from .models import User, Dataset
from datetime import datetime

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    '''
    form = LoginForm()
    if form.validate_on_submit():
        g.dataset.organism = form.species
        g.dataset.type = form.tech
        g.dataset.cell_line = form.cell_line
        g.dataset.treatment = form.drug
        g.gene = form.gene
        datasets = Dataset.query.filter_by(cell_line=form.cell_line).all()
        if datasets is None:
            flash("%s not found" % form.cell_line)
            return render_template('index.html',
                                   posts=posts,
                                   form=form)
        else:
            flash("%s found" % form.cell_line)
            return render_template('no_gene.html',
                                   datasets=datasets)
    else:
        flash('form.validate_on_submit() failed')
    '''


    return render_template('index.html')#,
                            #form=form)


@app.route('/search', methods=['POST'])
def search():
    cell_line = request.form['cell_line']
    drug = request.form['drug']
    ds = Dataset.query.filter_by(cell_line=cell_line).all()
    if ds:
        flash('%s found' % cell_line)
        return render_template('no_gene.html', datasets=ds)
    else:
        flash('No %s found' % cell_line)
        return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                            user=user,
                            posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)

