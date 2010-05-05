import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect_to
from pylons.decorators.secure import authenticate_form
from cgi import escape

from readlater.lib.helpers import flash
from readlater.lib.base import BaseController, render
from readlater.model import Item
from readlater.model.meta import Session

log = logging.getLogger(__name__)

class MainController(BaseController):

    def __before__(self):
        self.item_q = Session.query(Item)

    def index(self):
        # Return a rendered template
        #return render('/main.mako')
        # or, return a response
        return 'Hello World'

    def add(self):
        return render('/items/new.mako')
    
    def create(self):
        self.save(-1)
		
    def edit(self, id):
        """edit item with id
        """
        item = self.item_q.filter_by(id=id).first()
        if item:
            c.headline = item.headline
            c.desc = item.desc
            c.url = item.url
            c.status = item.status
        return render('/edit.mako')

    def save(self, id):
        """save item with id
        """
        item = self.item_q.filter_by(id=id).first()
        if not item:
            item = Item(request.params['headline'], request.params['url'])
        item.desc="dummy desc"
        Session.add(item)
        Session.commit()
        flash('Successfully saved %s!' % item.headline)
        redirect_to('unread_items')
	
    def delete(self, id):
        """delete item with id
        """
        item = self.item_q.filter_by(id=id).first()
        if not item:
            flash('Item with id %s not found' % id)
        Session.delete(item)
        Session.commit()
        flash('Deleted %s!' % item.headline)
        redirect_to('unread_items')

    def unread(self):
        """Displays unread items
        """
        #get list of all unread items
        c.items = self.item_q.all()
        return render('/items/unread.mako')

    def show(self, id):
        """Displays Item 
        """
        item = self.item_q.filter_by(id=id).first()
        if item:
            c.headline = item.headline
            c.desc = item.desc
            c.url = item.uri
            c.status = item.status
            return render('/items/show.mako')
        abort(404)