<%inherit file="/base.mako"/>\

<%def name="header()">Title List</%def>

<a href="${url('add_item')}">add item</a>
<ul id="items">
  % for item in c.items:
  <li>
    ${h.link_to(item.headline, item.uri)} 
    &nbsp; <a href="${url('show_item', id=item.id)}">detail</a>
    &nbsp; <a href="${url('delete_item', id=item.id)}">delete</a> 
  </li>
  % endfor
</ul>
