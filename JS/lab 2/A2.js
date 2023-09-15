// a-

function sumAll(numbersArray) {

	return numbersArray.join("+");
}


resultAllArr = eval(sumAll([3, 3, 3]))
console.log("sumAllArray:", resultAllArr)


// b-

function sumAlll() {

	arr = []

	for (var i = 0; i < arguments.length; i++) {

		arr.push(arguments[i])
	}
	return arr.join("+");
}

resultAll = eval(sumAlll(2, 2, 2))
console.log("sumAll:", resultAll)

