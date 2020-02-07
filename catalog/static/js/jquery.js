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

//INSTRUCTIONS OPEN
  $("#instructionsWelcome").click(function() {
    $(this).toggleClass("hide");
    $(this).siblings("#popupInstructionsWindowJQ").toggleClass("hide");
    // $(this).siblings("#popupGreyID").children().toggleClass("hide");

  });

//INSTRUCTIONS CLOSE
  $("#popupCloseButtonJQ").click(function() {
    // $(this).toggleClass("hide");
    $(this).parent().toggleClass("hide");
    $(this).parent().siblings("#instructionsWelcome").toggleClass("hide");

  });

//PROFILE PIC ICON CONFIRMATION
  $("#id_userpic").change(function() {
    // readURL(this);
    $('#profilePicConfirm').attr('src', 'https://db-hotspots-production.s3.us-east-2.amazonaws.com/profileImageConfirmCheckmark1.svg');
    $('#profilePicConfirm').css("visibility", "visible");
  });


// -- EXPERIMENTS
  $('#JQtest1').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest2').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest3').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest4').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest5').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest6').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest7').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest8').click(function() {
    $(this).toggleClass("customInputActive");
  });

  $('#JQtest9').click(function() {
    $(this).toggleClass("customInputActive");
  });




  //END DOC READY FUNCTION
  });
