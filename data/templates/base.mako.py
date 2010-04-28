# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272442707.568584
_template_filename=u'/Users/shiva/dev/workspace/readlater/readlater/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n<html>\n  <head>\n    <title>Readlater - reLoaded</title>\n  </head>\n\n  <body>\n    <div class="content">\n      <h1 class="main">')
        # SOURCE LINE 10
        __M_writer(escape(self.header()))
        __M_writer(u'</h1>\n      \n      ')
        # SOURCE LINE 12
        flashes = h.flash.pop_messages() 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['flashes'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 13
        if flashes:
            # SOURCE LINE 14
            for flash in flashes:
                # SOURCE LINE 15
                __M_writer(u'        <div id="flash">\n          <span class="message">')
                # SOURCE LINE 16
                __M_writer(escape(flash))
                __M_writer(u'</span>\n        </div>\n')
                pass
            pass
        # SOURCE LINE 20
        __M_writer(u'      \n      ')
        # SOURCE LINE 21
        __M_writer(escape(next.body()))
        __M_writer(u'')
        # SOURCE LINE 22
        __M_writer(u'      <p class="footer">\n        Return to the ')
        # SOURCE LINE 23
        __M_writer(escape(h.link_to('Home', url('unread_items'))))
        __M_writer(u'\n      </p>\n    </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


