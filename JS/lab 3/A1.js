var win = open("smallPage.html", "text", "width=300,height=350");
var text = "Welcome to js"
var letters = text.split("")
var i = 0

var interval = setInterval(function () {

	if (i < letters.length) {

		win.document.write(letters[i++])	
	}

	else {

		win.close()
	}

}, 300)