"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('home', '/', controller='main', action='show', title='Home')
    map.connect('unread_items', '/unread', controller='main', action='unread')
    map.connect('create_item', '/create', controller='main', action='create')
    map.connect('add_item', '/add', controller='main', action='add')
    map.connect('show_item', '/show/{id}', controller='main', action='show')
    map.connect('edit_item', '/edit/{id}', controller='main', action='edit')
    map.connect('save_item', '/save/{id}', controller='main', action='save', conditions=dict(method='POST'))
    map.connect('delete_item', '/delete/{id}', controller='main', action='delete')

    return map
