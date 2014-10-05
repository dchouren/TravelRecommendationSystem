function focusSearch(){
    document.getElementById("searchBox").focus();
}

$( document ).ready(function() {

	$("#searchBox").keyup(function(event){
		console.log('here');
	    if(event.keyCode == 13){
	        $("#addButton").trigger('click');
	    }
	});
})

