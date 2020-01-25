$("#clear_db").click(function(){
    $.ajax({
        url: 'http://localhost:3000/apis',
        type: 'DELETE',
        success: function(result) {
            // Do something with the result
        }
    });
});

function ajaxCall() {
    //do your AJAX stuff here
    $.get("http://localhost:3000/apis", function(data) {

        var data_length = data.length;
        // data_length = 3;
        $("#data_length").html(data_length);
        $("#content-container").empty();
        $.each(data, function(index, value){
            var item = "<p>" + index + " " + value.value + " " + value.timestamp + "</p>";
            $("#content-container").append(item);
        });
        // var data_array = JSON.parse(data);
        // var data_length = data_array.length;
        // test = {length: 3, data_array: [{"value": 23, "timestamp": "fake_time"}]}
        // data_array(!{data_array})

        // alert(data.length);
    });
}
setInterval(ajaxCall,3000);