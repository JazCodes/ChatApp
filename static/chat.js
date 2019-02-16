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


	$("#second").click(function() {
		console.log("Handler for .click() called.");
		var top10;
		$.get( "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty", function( data ) {
	  		next10 = data.slice(11,20);
	  		for(var i = 0; i < next10.length; i++) {
	  			var currenId = next10[i];
	  			$.get(`https://hacker-news.firebaseio.com/v0/item/${currenId}.json?print=pretty`, function ( data ) {
	  				$(" #second-string" ).append( `<div> ${data['title']} </div>`);
	  				console.log('line 35', next10);
	  			});

	  		}

		});
	});
});
});