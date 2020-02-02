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

//PROFILE PIC ICON CONFIRMATION
  $("#id_userpic").change(function() {
    // readURL(this);
    $('#profilePicConfirm').attr('src', 'https://db-hotspots-production.s3.us-east-2.amazonaws.com/profileImageConfirmCheckmark1.svg');
    $('#profilePicConfirm').css("visibility", "visible");
  });


  //END DOC READY FUNCTION
  });
