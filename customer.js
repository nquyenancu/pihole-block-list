$(document).ready(function(){
	console.log("OKE")
	document.getElementsByClassName('hope-c-PJLV-ihaOegS-css')[0].style.gridTemplateColumns='repeat(auto-fill, minmax(150px, 1fr))';
	const boxes = document.querySelectorAll('.hope-c-PJLV-iiRGVPv-css');

	boxes.forEach(box => {
	  box.style.height = 'auto';
	  box.style.width = '100%';
	});
});

function bindEvents(){
	console.log("bindEvents")
}