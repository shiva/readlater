<%inherit file="/base.mako"/>\

<%def name="header()">Editing ${c.headline}</%def>

${h.secure_form(url('save_page', title=c.id))}
  ${h.text_field(name='headline', content=c.headline)} <br />
  ${h.textarea(name='description', rows=7, cols=40, content=c.desc)} <br />
  ${h.text_field(name='status', content=c.status)} <br />
  ${h.submit(value='Save changes', name='commit')}
${h.end_form()}
