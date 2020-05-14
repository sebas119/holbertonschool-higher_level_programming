$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, textStatus, jqXHR) => {
    $('DIV#character').text(data.name);
  });
});
