# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272786876.8123269
_template_filename='/Users/shiva/dev/workspace/readlater/readlater/templates/items/unread.mako'
_template_uri='/items/unread.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n<a href="')
        # SOURCE LINE 5
        __M_writer(escape(url('add_item')))
        __M_writer(u'">add item</a>\n<ul id="items">\n')
        # SOURCE LINE 7
        for item in c.items:
            # SOURCE LINE 8
            __M_writer(u"  <div class='unread_item'>\n    ")
            # SOURCE LINE 9
            __M_writer(escape(h.link_to(item.headline, item.uri)))
            __M_writer(u' \n    &nbsp; <a href="')
            # SOURCE LINE 10
            __M_writer(escape(url('show_item', id=item.id)))
            __M_writer(u'">...</a>\n    &nbsp; <a href="')
            # SOURCE LINE 11
            __M_writer(escape(url('delete_item', id=item.id)))
            __M_writer(u'">X</a> \n  </div>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Title List')
        return ''
    finally:
        context.caller_stack._pop_frame()


