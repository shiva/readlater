<%inherit file="/base.mako"/>\

<%def name="header()">c.headline</%def>

${h.secure_form(url('save_item', id=-1))}
  Headline: ${h.text('headline')} <br />
  Description (optional): ${h.textarea(name='desc', rows=5, cols=40)} <br />
  Url: ${h.text('url')} <br />
  ${h.submit(value='Save', name='commit')}
${h.end_form()}