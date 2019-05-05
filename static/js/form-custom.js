var post_form = function(){
	let url 	= "/form-submission"
	let data 	= $('form').serializeArray()
	console.log(data)
	$.post(url, data, function(redirect_url, status){
		console.log(`${redirect_url} and ${status}`)
		window.location.href = redirect_url
	})
}