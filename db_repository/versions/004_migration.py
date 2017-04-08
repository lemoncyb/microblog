from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
cell__line = Table('cell__line', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('cell_line', String(length=100)),
)

dataset = Table('dataset', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dir_name', String(length=50)),
    Column('pmid', Integer),
    Column('journal', String(length=100)),
    Column('year', String(length=50)),
    Column('organism', String(length=30)),
    Column('initial_condition', String(length=300)),
    Column('cell_line', String(length=100)),
    Column('type', String(length=10)),
    Column('library', String(length=200)),
    Column('norm_method', String(length=100)),
    Column('treatment', String(length=200)),
    Column('culture_days', Integer),
    Column('sample', String(length=200)),
    Column('is_initial_condition', Boolean),
    Column('source', String(length=50)),
    Column('first_author', String(length=100)),
    Column('last_author', String(length=100)),
    Column('title', String(length=500)),
    Column('contact', String(length=100)),
    Column('public_status', String(length=100)),
)

library = Table('library', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('library', String(length=200)),
    Column('addgene_id', String(length=100)),
    Column('type', String(length=40)),
    Column('species', String(length=100)),
    Column('lenti_gen', String(length=50)),
    Column('pi', String(length=200)),
    Column('genes_targeted', Integer),
    Column('grnas_per_gene', Integer),
    Column('total_grans', Integer),
)

publication = Table('publication', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('pmid', Integer),
    Column('journal', String(length=100)),
    Column('year', String(length=50)),
    Column('first_author', String(length=100)),
    Column('last_author', String(length=100)),
    Column('title', String(length=500)),
)

sample = Table('sample', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dir_name', String(length=50)),
    Column('publication_id', Integer),
    Column('organism', String(length=30)),
    Column('initial_condition', String(length=300)),
    Column('cell_line_id', Integer),
    Column('type', String(length=10)),
    Column('library_id', Integer),
    Column('norm_method', String(length=100)),
    Column('treatment', String(length=200)),
    Column('culture_days', Integer),
    Column('sample', String(length=200)),
    Column('is_initial_condition', Boolean),
    Column('source', String(length=50)),
    Column('contact', String(length=100)),
    Column('public_status', String(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['cell__line'].create()
    post_meta.tables['dataset'].create()
    post_meta.tables['library'].create()
    post_meta.tables['publication'].create()
    post_meta.tables['sample'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['cell__line'].drop()
    post_meta.tables['dataset'].drop()
    post_meta.tables['library'].drop()
    post_meta.tables['publication'].drop()
    post_meta.tables['sample'].drop()
