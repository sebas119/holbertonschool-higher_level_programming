$(document).ready(function () {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`, (data, textStatus, jqXHR) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
