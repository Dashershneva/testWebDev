/*$(function() {
	var $h1 = $('h1.class-a'),
		showed = true;
	$('.btn').click(function () {
		if(showed){
			$h1.hide();
		}
		else {
			$h1.show();
		}
		
		showed = !showed
			 
		return false;
	});
	
}); */

$(function () {
	var $btn = $('.update-button');
	
	$btn.click(function () {
		alert('Hello, world');
	});
});