$( document ).ready(function() {
    function fetch (){

    	$.get("/chatapp", function (data){
    		console.log(data);

    		$(".messages").empty();
    		data.forEach((x) => {
    			$(".messages").append(`<div>${x}</div>`);
    			
    		});
    	});
    }

    function init() {
    	setInterval(function(){fetch(); }, 5000);

    }

    init();
});



$( document ).ready(function() {
    $('#messages', function(data){
      $.ajax({
      type: 'GET', 
      url: '~/'
      data: {text, text}
    }).done(function( o ){
      $('#messages' ).append( `<p>${data}</p>` );
    });
});
    $.setInterval(ajax(), 1000);
});
