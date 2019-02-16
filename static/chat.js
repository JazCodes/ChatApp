$( document ).ready(function() {
	console.log( "ready!" );

	$("#target").click(function() {
		console.log("Handler for .click() called.");
		$.get( "/string", function( data ) {
	  		$( "#random-string" ).html( data );
		});
	});
});


