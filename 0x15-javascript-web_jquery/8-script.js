$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus, jqXHR) => {
    const results = $.map(data.results, (item) => item.title);
    $.each(results, (index, value) => {
      $('UL#list_movies').append(`<li>${value}</li>`);
    });
  });
});
