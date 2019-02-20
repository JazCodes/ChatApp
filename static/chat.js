// $( document ).ready(function() {
//     function fetch (){

//     	$.get("/chatapp", function (data){
//     		console.log(data);

//     		$(".messages").empty();
//     		data.forEach((x) => {
//     			$(".messages").append(`<div>${x}</div>`);
    			
//     		});
//     	});
//     }

//     function init() {
//     	setInterval(function(){fetch(); }, 5000);

//     }

//     init();
// });


$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#nameInput').val(),
				message : $('#messageInput').val()
			},
			type : 'POST',
			url : '/'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});