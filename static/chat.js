$( document ).ready(function() {
	console.log( "ready!" );
	var randomStringData;

	$("#target").click(function() {
		console.log("Handler for .click() called.");
		var top10;
		$.get( "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty", function( data ) {
	  		top10 = data.slice(0,10);
	  		console.log('Line 11', top10);
	  		for(var i = 0; i < top10.length; i++) {
	  			var currId = top10[i];
	  			$.get(`https://hacker-news.firebaseio.com/v0/item/${currId}.json?print=pretty`, function ( data ) {
	  				$(" #random-string" ).append( `<div> ${data['title']} </div>`);

	  			});

	  		}

		});
		console.log('Line 14', top10);
	});
});


