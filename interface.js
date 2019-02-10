$( document ).ready(function() {

    $('.btn').on('click', function() {
    	// $('button').removeClass('active');
    	$(this).addClass('active');
    	getInput()
	})

});

$('#debugSelector').click(function() {
    	// $('button').removeClass('active');
    	getInput()
    	console.log($("#info1").val())
})

$('#show-results').click(function() {
    	// $('button').removeClass('active');
    	getInput()
    	console.log($("#info1").val())
})

function getInput(){
	var list = [];
	list.push($("#info1").val())
	list.push($("#info2").val())
	list.push($("#info3").val())
	list.push($("#info4").val())
	list.push($("#info5").val())
	list.push($("#info6").val())
	list.push($("#info7").val())
	list.push($("#info8").val())
	list.push($("#info9").val())
	console.log("list is " + list);
}

// getInput();
