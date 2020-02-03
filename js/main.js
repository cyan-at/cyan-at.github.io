var sounds = {};
var blackboard = {
  "active_howl_id" : ""
};

$(document).ready(function(){
  // $('#links').flowtype({
  //    // minimum : 50,
  //    // maximum : 500
  //    // fontRatio : 30
  //    minFont : 8,
  //    maxFont : 15
  // });

  lazyload();

  latest_example_toggler_href_to_latest_id = {};

  $('.example_toggler').click(function(event) {
    var href = $(event.target).attr('href');

    /*
    // if ID exists and it is the last source ID
    // toggle, otherwise update last source ID
    var id_attr = $(event.target).attr('id');
    if (typeof id_attr !== "undefined" && id_attr !== false) {
      if (href in latest_example_toggler_href_to_latest_id) {
        if (latest_example_toggler_href_to_latest_id[href] == id_attr) {
          $(href).toggle();
        }
      } else {
        $(href).toggle();
      }
      latest_example_toggler_href_to_latest_id[href] = id_attr;
    } else {
      $(href).toggle();
      // latest_example_toggler_href_to_latest_id.clear();
    }
    */

    $(href).toggle();

    // $('.toggle_example').hide();
    // $(href).show();

    // if ($(href).is(":visible")) {
    //   $(href).hide();
    // } else {
    //   $(href).show();
    // }
  });


  $("#reset").click(function(event) {
    $('.toggle_example').hide();
  });

  // id to Howl objects to play
  $('.lazy_play_sound').click(function(event) {
    var howl_id = $(event.target).attr('howl_id');
    var mp3_path = $(event.target).attr('mp3_path');
    // "lazy"
    if (sounds.hasOwnProperty(howl_id)) {
      console.log("found sound");
    } else {
      console.log("lazy loading sound " + howl_id);
      sounds[howl_id] = new Howl({
        src: [mp3_path],
        // onplayerror: function() {
        //   sound.once('unlock', function() {
        //     sound.play();
        //   });
        // }


        onend: function() {
          console.log('finished playing song');

          // put into stopped state
          $(this).text("*Play");

          // hygiene
          blackboard["active_howl_id"] = "";
        }
      });
    }

    // hygiene
    if (blackboard["active_howl_id"] != "") {
      var active_howl_id = blackboard["active_howl_id"];
      if (sounds.hasOwnProperty(active_howl_id)) {
        sounds[active_howl_id].stop();
      }
      blackboard["active_howl_id"] = "";
    }

    // state is opposite of text i.e. play == stopped state
    var this_state = $(this).text();
    if (this_state == "*Play") {
      sounds[howl_id].play();

      $(this).text("*Stop");
    } else {
      sounds[howl_id].pause();

      $(this).text("*Play");
    }
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

/*
https://stackoverflow.com/questions/3698200/window-onload-vs-document-ready

The ready event occurs after the HTML document has been loaded
while the onload event occurs later, when all content (e.g. images) also has been loaded.

The onload event is a standard event in the DOM,
while the ready event is specific to jQuery.
The purpose of the ready event is that it should occur as
early as possible after the document has loaded,
so that code that adds functionality to the elements
in the page doesn't have to wait for all content to load.
*/