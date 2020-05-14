$(document).ready(function () {

  const request = () => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`, (data, textStatus, jqXHR) => {
      $('DIV#hello').html(data.hello);
    });
  }
  $('INPUT#btn_translate').on('click', request);
  $('INPUT#language_code').on('keypress', (e) => {
    if (e.which === 13) request();
  });

});
