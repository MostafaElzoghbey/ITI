var i = 1

var interval = setInterval(function () {

	window.document.title = `${i}`
	window.document.write(`<div class="n${i}"> ${i} </div>
		<style>
			.n${i} {
				width: fit-content;
				height: fit-content;
				border: 5px double red;
				text-align: center;
				padding: 1px;
			}
		</style>`);

	i++;

}, 300)
