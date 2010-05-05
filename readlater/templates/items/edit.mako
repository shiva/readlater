<%inherit file="/base.mako"/>\

<%def name="header()">Editing ${c.headline}</%def>

${h.secure_form(url('save_page', title=c.id))}
  ${h.text_field(name='headline', content=c.headline)} <br />
  ${h.textarea(name='description', rows=7, cols=40, content=c.desc)} <br />
  ${h.text_field(name='status', content=c.status)} <br />
  ${h.submit(value='Save changes', name='commit')}
${h.end_form()}


${h.secure_form(url('save_item', id=-1))}
  Url: <br />${h.text('url')} <br />
  Headline: <br />${h.text('headline')} <br />
  Description (optional): <br />${h.textarea(name='desc', rows=5, cols=40)} <br />
  ${h.submit(value='Save', name='commit')}
${h.end_form()}