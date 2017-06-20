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
            // console.log(result);
            var json_response = JSON.parse(result);
            console.log("The json version: " + json_response.prediction);
            $("#mnist-output").html("<h3>"+result+"</h3>" +
                "<div class='row'>" +
                "<div class='col-xs-4'>" +
                "<div class='table-responsive'>" +
                "<table class='table'> " +
                "<thead>" +
                "<tr> " +
                "<th>Num</th>" +
                "<th>Prob</th>" +
                "</tr>" +
                "</thead> " +
                "<tbody>" +
                "<tr> " +
                "<td>0</td> " +
                "<td>" + json_response.probabilities[0] + "</td>" +
                "</tr>" +
                "</tbody>" +
                "</table>" +
                "</div>" +
                "</div>" +
                "<div class='col-xs-4'>" +
                "<img class='img-responsive' src='"+ url +"'/>" +
                "</div>" +
                "</div>");
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
            $("#cifar10-output").html("<h3>"+result+"</h3>" +
                "<div class='row'>" +
                "<div class='col-xs-4 col-xs-offset-4'>" +
                "<img class='text-center img-responsive' src='"+ url +"'/>" +
                "</div> " +
                "</div>");
        },
    });
});