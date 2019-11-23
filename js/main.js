$(document).ready(function(){
  // $('#links').flowtype({
  //    // minimum : 50,
  //    // maximum : 500
  //    // fontRatio : 30
  //    minFont : 8,
  //    maxFont : 15
  // });

  lazyload();

  $('.example_toggler').click(function(event) {
    var href = $(event.target).attr('href');

    // $('.toggle_example').hide();
    // $(href).show();

    $(href).toggle();
    // if ($(href).is(":visible")) {
    //   $(href).hide();
    // } else {
    //   $(href).show();
    // }
  });


  $("#reset").click(function(event) {
    $('.toggle_example').hide();
  });
});

// #cool handle anchor links that reference hidden divs
window.onload = function() {

  var hash = window.location.hash;
  if(hash != "") {
    var id = hash.substr(1); // get rid of #
    document.getElementById(id).style.display = 'block';
  }
};