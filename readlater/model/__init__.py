"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from readlater.model import meta

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine


## Non-reflected tables may be defined and mapped at module level
items_table = sa.Table('Items', meta.metadata,
	sa.Column('id', sa.types.Integer, primary_key=True),
	sa.Column('headline', sa.types.Unicode(), nullable=false),
	sa.Column('uri', sa.types.Unicode(), nullable=false),
	sa.Column('status', sa.types.Integer, nullable=false, default=0),
	)
# status 
# 0 - unread
# 1 - read
# 2 - archived
# 3 - deleted
class Item(object):
	
	def __init__(self, headline, uri, status=0):
		self.headline = headline
		self.uri = uri
		self.status = status
		
	def __unicode__(self):
		return self.headline
		
	__str__ = __unicode__

orm.mapper(Item, items_table)
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
