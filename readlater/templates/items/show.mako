<%inherit file="/base.mako"/>\

<%def name="header()">c.headline</%def>
Id: ${c.id} <br />
Headline: ${c.headline} <br />
Url: ${h.link_to(c.url, c.url)} <br />
Desc : ${h.literal(c.desc)} <br />
Status: ${c.status} <br />