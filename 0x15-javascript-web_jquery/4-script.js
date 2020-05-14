$(document).ready(function () {
  let currentClass;
  $('#toggle_header').click(function () {
    currentClass = $('header').attr('class');
    if (currentClass === 'green') {
      $('header').addClass('red').removeClass('green');
    } else {
      $('header').addClass('green').removeClass('red');
    }
  });
});
