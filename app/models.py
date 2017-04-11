from app import db
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s/%d' % (md5(self.email.encode('utf-8')).hexdigest, size)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dir_name = db.Column(db.String(50), index=True)
    pmid = db.Column(db.Integer, index=True)
    journal = db.Column(db.String(100), index=True)
    year = db.Column(db.String(50), index=True)
    species = db.Column(db.String(30), index=True)
    initial_condition = db.Column(db.String(300), index=True)
    cell_line = db.Column(db.String(100), index=True)
    type = db.Column(db.String(10), index=True)
    library = db.Column(db.String(200), index=True)
    norm_method = db.Column(db.String(100), index=True)
    treatment = db.Column(db.String(200), index=True)
    other_condition = db.Column(db.String(200), index=True)
    culture_days = db.Column(db.Integer, index=True)
    sample = db.Column(db.String(200), index=True)
    is_initial_condition = db.Column(db.Boolean, index=True)
    source = db.Column(db.String(50), index=True)
    first_author = db.Column(db.String(100), index=True)
    last_author = db.Column(db.String(100), index=True)
    title = db.Column(db.String(500), index=True)
    contact = db.Column(db.String(100), index=True)
    public_status = db.Column(db.String(100), index=True)

    def __repr__(self):
        return '<Dataset %r>' % (self.dir_name)


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dir_name = db.Column(db.String(50), index=True)
    publication_id = db.Column(db.Integer, index=True)
    species = db.Column(db.String(30), index=True)
    initial_condition = db.Column(db.String(300), index=True)
    cell_line_id = db.Column(db.Integer, index=True)
    type = db.Column(db.String(10), index=True)
    library_id = db.Column(db.Integer, index=True)
    norm_method = db.Column(db.String(100), index=True)
    treatment = db.Column(db.String(200), index=True)
    other_condition = db.Column(db.String(200), index=True)
    culture_days = db.Column(db.Integer, index=True)
    sample = db.Column(db.String(200), index=True)
    is_initial_condition = db.Column(db.Boolean, index=True)
    source = db.Column(db.String(50), index=True)
    contact = db.Column(db.String(100), index=True)
    public_status = db.Column(db.String(100), index=True)

    def __repr__(self):
        return '<Sample %r>' % (self.dir_name)


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pmid = db.Column(db.Integer, index=True)
    journal = db.Column(db.String(100), index=True)
    year = db.Column(db.String(50), index=True)
    first_author = db.Column(db.String(100), index=True)
    last_author = db.Column(db.String(100), index=True)
    title = db.Column(db.String(500), index=True)

    def __repr__(self):
        return '<Publication %r>' % (self.pmid)


class Cell_Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cell_line = db.Column(db.String(100), index=True)

    def __repr__(self):
        return '<Cell_Line %r>' % (self.cell_line)


class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    library = db.Column(db.String(200), index=True)
    addgene_id =db.Column(db.String(100), index=True)
    type = db.Column(db.String(40), index=True)
    species = db.Column(db.String(100), index=True)
    lenti_gen = db.Column(db.String(50), index=True)
    pi = db.Column(db.String(200), index=True)
    genes_targeted = db.Column(db.Integer, index=True)
    grnas_per_gene = db.Column(db.Integer, index=True)
    total_grans = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Library %r>' % (self.library)