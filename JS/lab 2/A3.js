
function getMonth(particDate) {
	
	return particDate.split(" ")[1]
}

var Dat = new Date();
Month = getMonth(Dat.toString())
console.log("Month from getMonth:", Month)


function convToMonth(DateString) {

	MonthsList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	MonthIndx = DateString[0]
	console.log("Month from convToMonth:", MonthsList[MonthIndx - 1])
}


convToMonth(Dat.toLocaleString())



