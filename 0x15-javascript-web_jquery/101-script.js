$(document).ready(function () {
  const uList = $('UL.my_list');
  $('DIV#add_item').click(function () {
    uList.append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('LI', uList).last().remove();
  });
  $('DIV#clear_list').click(function () {
    uList.empty();
  });
});
