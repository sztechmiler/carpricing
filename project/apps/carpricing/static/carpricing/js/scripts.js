/*!
    * Start Bootstrap - Creative v6.0.1 (https://startbootstrap.com/themes/creative)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-creative/blob/master/LICENSE)
    */
    (function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 72)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 75
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-scrolled");
    } else {
      $("#mainNav").removeClass("navbar-scrolled");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

  // Magnific popup calls
  $('#portfolio').magnificPopup({
    delegate: 'a',
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1]
    },
    image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
    }
  });

})(jQuery); // End of use strict

//API Request
const verseChoose = document.querySelector('select', '#id_Marka');
const answer = document.querySelector('#id_Model');

verseChoose.onchange = function() {
    const marka = this.value;
    makeApiCall('/api/' + marka);
};

function makeApiCall(url){
    fetch(url).then(function(response) {
    response.json().then(function(data) {
      $('#id_Model').empty();
      $.each(data["brandModels"], function(i, p) {
          $('#id_Model').append($('<option></option>').val(p).html(p));
      });
  });
});
}




$(document).ready(function() {
  $('#quote_form').submit(function() { // catch the form's submit event
      let parameters = $(this).serialize()
      $.ajax({ // create an AJAX call...
          type: "GET", // GET or POST
          url: window.location.origin + "/api/?" + parameters , // the file to call
          success: function(response) { // on success..
              $('#quote_div').html(response); // update the DIV 
          }
      });
      return false;
  });
});