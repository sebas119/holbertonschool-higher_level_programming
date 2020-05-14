$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus, jqXHR) => {
    $('DIV#hello').text(data.hello);
  });
});
