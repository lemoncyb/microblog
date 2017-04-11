from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
dataset = Table('dataset', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('dir_name', VARCHAR(length=50)),
    Column('pmid', INTEGER),
    Column('journal', VARCHAR(length=100)),
    Column('year', VARCHAR(length=50)),
    Column('organism', VARCHAR(length=30)),
    Column('initial_condition', VARCHAR(length=300)),
    Column('cell_line', VARCHAR(length=100)),
    Column('type', VARCHAR(length=10)),
    Column('library', VARCHAR(length=200)),
    Column('norm_method', VARCHAR(length=100)),
    Column('treatment', VARCHAR(length=200)),
    Column('culture_days', INTEGER),
    Column('sample', VARCHAR(length=200)),
    Column('is_initial_condition', BOOLEAN),
    Column('source', VARCHAR(length=50)),
    Column('first_author', VARCHAR(length=100)),
    Column('last_author', VARCHAR(length=100)),
    Column('title', VARCHAR(length=500)),
    Column('contact', VARCHAR(length=100)),
    Column('public_status', VARCHAR(length=100)),
    Column('other_condition', VARCHAR(length=200)),
)

dataset = Table('dataset', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dir_name', String(length=50)),
    Column('pmid', Integer),
    Column('journal', String(length=100)),
    Column('year', String(length=50)),
    Column('species', String(length=30)),
    Column('initial_condition', String(length=300)),
    Column('cell_line', String(length=100)),
    Column('type', String(length=10)),
    Column('library', String(length=200)),
    Column('norm_method', String(length=100)),
    Column('treatment', String(length=200)),
    Column('other_condition', String(length=200)),
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

sample = Table('sample', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('dir_name', VARCHAR(length=50)),
    Column('publication_id', INTEGER),
    Column('organism', VARCHAR(length=30)),
    Column('initial_condition', VARCHAR(length=300)),
    Column('cell_line_id', INTEGER),
    Column('type', VARCHAR(length=10)),
    Column('library_id', INTEGER),
    Column('norm_method', VARCHAR(length=100)),
    Column('treatment', VARCHAR(length=200)),
    Column('culture_days', INTEGER),
    Column('sample', VARCHAR(length=200)),
    Column('is_initial_condition', BOOLEAN),
    Column('source', VARCHAR(length=50)),
    Column('contact', VARCHAR(length=100)),
    Column('public_status', VARCHAR(length=100)),
    Column('other_condition', VARCHAR(length=200)),
)

sample = Table('sample', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dir_name', String(length=50)),
    Column('publication_id', Integer),
    Column('species', String(length=30)),
    Column('initial_condition', String(length=300)),
    Column('cell_line_id', Integer),
    Column('type', String(length=10)),
    Column('library_id', Integer),
    Column('norm_method', String(length=100)),
    Column('treatment', String(length=200)),
    Column('other_condition', String(length=200)),
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
    pre_meta.tables['dataset'].columns['organism'].drop()
    post_meta.tables['dataset'].columns['species'].create()
    pre_meta.tables['sample'].columns['organism'].drop()
    post_meta.tables['sample'].columns['species'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['dataset'].columns['organism'].create()
    post_meta.tables['dataset'].columns['species'].drop()
    pre_meta.tables['sample'].columns['organism'].create()
    post_meta.tables['sample'].columns['species'].drop()
