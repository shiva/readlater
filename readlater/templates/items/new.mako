<%inherit file="/base.mako"/>\

<%def name="header()">Add Item</%def>
<form name="test" method="GET" action="/create">
Url: <br /> <input type="text" name="url" /> <br />
Title: <br /> <input type="text" name="headline" /> <br />
Summary: <br /> <textarea rows=7 cols=100 name="desc"></textarea> <br />

<input type="submit" name="submit" value="Submit" />
</form>
