/**
 * Created by benji on 6/8/17.
 */

$(document).on('click','#mnist-submit',function () {

    console.log("clicked on submit!");
    var url = $('#mnist-input-url').val();
    console.log(url);
    //set output to processing gif while we wait for ajax response
    var gif =  "<div class='text-center'> Processing...<br/><img class='text-center' src='https://railsgirlssummerofcode.org/img/blog/2016/l1ghtsab3r-partyparrot.gif'/> </div>";
    $("#mnist-output").html(gif);
    $.ajax({
        url:'/api/mnist',
        method: 'POST',
        contentType: 'text/plain',
        data: url,
        success: function(result){
            $("#mnist-output").html("<h3>"+result+"</h3>");
        },
    });
});

$(document).on('click','#cifar10-submit',function () {

    console.log("clicked on submit!");
    var url = $('#cifar10-input-url').val();
    console.log(url);
    //set output to processing gif while we wait for ajax response
    var gif =  "<div class='text-center'> Processing...<br/><img class='text-center' src='https://railsgirlssummerofcode.org/img/blog/2016/l1ghtsab3r-partyparrot.gif'/> </div>";
    $("#cifar10-output").html(gif);
    $.ajax({
        url:'/api/cifar10',
        method: 'POST',
        contentType: 'text/plain',
        data: url,
        success: function(result){
            $("#cifar10-output").html("<h3>"+result+"</h3>");
        },
    });
});