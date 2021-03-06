/**
 * Created by benji on 6/8/17.
 */

$(document).on('click','#mnist-submit',function () {

    console.log("clicked on submit!");
    var url = $('#mnist-input-url').val();
    console.log(url);
    //set output to processing gif while we wait for ajax response
    var gif =  "<div class='text-center'> Processing...<br/><img class='text-center' src='https://railsgirlssummerofcode.org/img/blog/2016/l1ghtsab3r-partyparrot.gif'/> </div>";
    $("#mnist-output-img").html(gif);
    $.ajax({
        url:'/api/mnist',
        method: 'POST',
        contentType: 'text/plain',
        data: url,
        success: function(result){
            // console.log(result);
            var json_response = JSON.parse(result);
            console.log("The json prediction: " + json_response.probabilities);
            var probabilites = json_response.probabilities;
            $("#mnist-output-img").html("<h3>Prediction: " + json_response.prediction +"</h3>" +
                "<img class='img-responsive' src="+ url +" />");
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
            var json_response = JSON.parse(result);
            $("#cifar10-output").html("<h3>"+"Prediction: " + json_response.prediction + "</h3>" +
                "<div class='row'>" +
                "<div class='col-xs-4 col-xs-offset-4'>" +
                "<img class='text-center img-responsive' src='"+ url +"'/>" +
                "</div> " +
                "</div>");
        },
    });
});