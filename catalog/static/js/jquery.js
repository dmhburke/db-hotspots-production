$(document).ready(function() {

  // ENTER REVIEW on ADDDETAIL page
    $("#addDetailsButton").click(function() {
      $("#detailsFormContainer").toggleClass("detailsFormContainerOpen");
      $("#addDetailsButton").toggleClass("detailButtonActive");
    });

    // ENTER REVIEW 'active' vibe entries
    // $("label").click(function() {
    //     $(this).addClass('labelActive');
    // });

    $("label").click(function () {
            $(this).parent("#detailsPerfectForItem").addClass("labelActive");
    });


  // BROWSE Function to display all activity vs my activity
  $('#browseMySpotsScrollContainer').hide();
  $('#browseWishlistScrollContainer').hide();

  $('#browseButton1').click(function() {
    $(this).addClass('activeBrowseButton');
    $(this).siblings().removeClass('activeBrowseButton');
    $(this).parent().siblings('#browseAllSpotsScrollContainer').show();
    $(this).parent().siblings('#browseMySpotsScrollContainer').hide();
    $(this).parent().siblings('#browseWishlistScrollContainer').hide();
    });
  $('#browseButton2').click(function() {
    $(this).addClass('activeBrowseButton');
    $(this).siblings().removeClass('activeBrowseButton');
    $(this).parent().siblings('#browseAllSpotsScrollContainer').hide();
    $(this).parent().siblings('#browseMySpotsScrollContainer').show();
    $(this).parent().siblings('#browseWishlistScrollContainer').hide();
    });
  $('#browseButton3').click(function() {
    $(this).addClass('activeBrowseButton');
    $(this).siblings().removeClass('activeBrowseButton');
    $(this).parent().siblings('#browseAllSpotsScrollContainer').hide();
    $(this).parent().siblings('#browseMySpotsScrollContainer').hide();
    $(this).parent().siblings('#browseWishlistScrollContainer').show();
    });

  //INSTRUCTIONS CLOSE/ OPEN

  $("#instructionsWelcome").click(function() {
    $(this).toggleClass("hide");
    $(this).siblings("#popupGreyID").toggleClass("hide");
    $(this).siblings("#popupGreyID").children().toggleClass("hide");

  });

  $("#popupGreyCloseID").click(function() {
    $(this).toggleClass("hide");
    $(this).parent().toggleClass("hide");
    $(this).parent().siblings("#instructionsWelcome").toggleClass("hide");

  });



  //END DOC READY FUNCTION
  });


//   //

//
//   $("#testfunction").click(function() {
//   if /* if we're on iOS, open in Apple Maps */
//     ((navigator.platform.indexOf("iPhone") != -1) ||
//      (navigator.platform.indexOf("iPad") != -1) ||
//      (navigator.platform.indexOf("iPod") != -1))
//     window.open("https://www.google.com/maps/d/u/0/edit?hl=en&hl=en&mid=1zBhX7397l1_VDdueypHfXqawYpJoI12-&ll=33.55310721216972%2C-111.83654260338062&z=11");
// else /* else use Google */
//     window.open("https://www.google.com/maps/d/u/0/edit?hl=en&hl=en&mid=1zBhX7397l1_VDdueypHfXqawYpJoI12-&ll=33.55310721216972%2C-111.83654260338062&z=11");
// }
//
//   });
//
//
//
// /*
//
// $("label").click(function() {
//   $(this).css({
//     "background-color": "#1e8eff",
//     "color": "white"
//   });
// });
//
// .toggleClass("perfectActive");
//
//
//
//   .css({
//     "background-color": "#1e8eff",
//     "color": "white"
//   });
//
//
// $("#hitlistButton").click(function() {
//   $(this).css({
//     "background-color": "#f2f2f2",
//     "color": "#1e8eff"
//   });
//   $("#wishlistButton").css({
//     "background-color": "#b7b5b5",
//     "color": "#f2f2f2"
//   });
//   $("#hitlistResultsUserpage").css("width", "340px");
//   $("#wishlistResultsUserpage").css("width", "0px");
// });
//
// $("#wishlistButton").click(function() {
//   $(this).css({
//     "background-color": "#f2f2f2",
//     "color": "#1e8eff"
//   });
//   $("#hitlistButton").css({
//     "background-color": "#b7b5b5",
//     "color": "#f2f2f2"
//   });
//   $("#wishlistResultsUserpage").css("width", "340px");
//   $("#hitlistResultsUserpage").css("width", "0px");
// });
//
// $("#hitlistButtonUser").click(function() {
//   $(this).css({
//     "background-color": "#f2f2f2",
//     "color": "#1e8eff"
//   });
//   $("#wishlistButtonUser").css({
//     "background-color": "#b7b5b5",
//     "color": "#f2f2f2"
//   });
//   $("#hitlistResultsUser").css("width", "340px");
//   $("#wishlistResultsUser").css("width", "0px");
// });
//
// $("#wishlistButtonUser").click(function() {
//   $(this).css({
//     "background-color": "#f2f2f2",
//     "color": "#1e8eff"
//   });
//   $("#hitlistButtonUser").css({
//     "background-color": "#b7b5b5",
//     "color": "#f2f2f2"
//   });
//   $("#wishlistResultsUser").css("width", "340px");
//   $("#hitlistResultsUser").css("width", "0px");
// });
//
//
// $("#hitlistButtonDiscover").click(function() {
//   $(this).css({
//     "background-color": "#f2f2f2",
//     "color": "#1e8eff"
//   });
//   $("#wishlistButtonDiscover").css({
//     "background-color": "#b7b5b5",
//     "color": "#f2f2f2"
//   });
//   $("#hitlistResultsDiscover").css("width", "340px");
//   $("#wishlistResultsDiscover").css("width", "0px");
// });
//
// $("#wishlistButtonDiscover").click(function() {
//   $(this).css({
//     "background-color": "#f2f2f2",
//     "color": "#1e8eff"
//   });
//   $("#hitlistButtonDiscover").css({
//     "background-color": "#b7b5b5",
//     "color": "#f2f2f2"
//   });
//   $("#wishlistResultsDiscover").css("width", "340px");
//   $("#hitlistResultsDiscover").css("width", "0px");
// });
//
// $("#detailHitlistButton").click(function() {
//   $("#detailsRatingBox").css("height: 200px");
// });
// */
