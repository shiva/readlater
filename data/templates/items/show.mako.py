# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272443740.3029301
_template_filename='/Users/shiva/dev/workspace/readlater/readlater/templates/items/show.mako'
_template_uri='/items/show.mako'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\nId: ')
        # SOURCE LINE 4
        __M_writer(escape(c.id))
        __M_writer(u' <br />\nHeadline: ')
        # SOURCE LINE 5
        __M_writer(escape(c.headline))
        __M_writer(u' <br />\nUrl: ')
        # SOURCE LINE 6
        __M_writer(escape(h.link_to(c.url, c.url)))
        __M_writer(u' <br />\nDesc : ')
        # SOURCE LINE 7
        __M_writer(escape(h.literal(c.desc)))
        __M_writer(u' <br />\nStatus: ')
        # SOURCE LINE 8
        __M_writer(escape(c.status))
        __M_writer(u' <br />')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'c.headline')
        return ''
    finally:
        context.caller_stack._pop_frame()


