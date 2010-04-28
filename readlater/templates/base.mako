<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
  <head>
    <title>Readlater - reLoaded</title>
  </head>

  <body>
    <div class="content">
      <h1 class="main">${self.header()}</h1>
      
      <% flashes = h.flash.pop_messages() %>
      % if flashes:
        % for flash in flashes:
        <div id="flash">
          <span class="message">${flash}</span>
        </div>
        % endfor
      % endif
      
      ${next.body()}\
      <p class="footer">
        Return to the ${h.link_to('Home', url('unread_items'))}
      </p>
    </div>
  </body>
</html>
