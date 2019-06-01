"use strict";

$(document).ready(function () {
  $('body').attr('aria-busy', true);
  $('#preloader-markup').load('mdb.css-addons/preloader.html', function () {
    $(window).on('load', function () {
      $('#mdb.css-preloader').fadeOut('slow');
      $('body').removeAttr('aria-busy');
    });
  });
});