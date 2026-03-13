/*!
 * Item: Kitzu
 * Description: Personal Portfolio Template
 * Author/Developer: Exill
 * Author/Developer URL: https://themeforest.net/user/exill
 * Version: v2.0.1
 * License: Themeforest Standard Licenses: https://themeforest.net/licenses
 */

/*----------- CUSTOM JS SCRIPTS -----------*/

(function($) {
  'use strict';
  $(function() {
    if (window.location.hash === "#contact") {
        var contactLink = $('.navbar .navbar-nav .nav-link[href="#contact"]');
        if (contactLink.length) {
            contactLink.trigger('click'); // triggers animatedModal to open
        }
    }
  });
  $(window).on('load', function() {
    // Code here executes When the page is loaded
  });
}(jQuery));