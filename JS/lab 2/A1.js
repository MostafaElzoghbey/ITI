
var arr = [3, 1, 2, 4, 3, 5, 1];


function _remove(arr, indx) {
		
	newArr = [];
	
	for (var i = 0; i < arr.length; i++) {
		
		if (i != indx) {
			
			newArr.push(arr[i]);
		}
	}
	
	return newArr;
}


// Write a JavaScript code to remove duplicate items from an array.

function _rmDup(arr) {
	
	for (var i = 0; i < arr.length - 1; i++) {
		
		for (var j = i + 1; j < arr.length; j++) {
			
			if (arr[i] === arr[j]) {
				
				arr = _remove(arr, j);
			}
		}
	}
	
	return arr;
}

console.log("array            :", arr);
arr = _rmDup(arr);
console.log("array after reDup:", arr);


// Sort them ascending

arr.sort(function (i, j){

	return i - j

})

console.log("array after sort ascending:", arr);


// Filter numbers larger than 50
// a- User defined function

function userFilter(arr) {

	for (var i = 0; i < arr.length; i++) {

		if (arr[i] > 50) {
			
			arr = _remove(arr, i);
		}
	}

	return arr
}

console.log("array before user filter:", arr);
arr = userFilter(arr)
console.log("array after user filter:", arr);


// Filter numbers larger than 50
// b- Array built in filter function

console.log("array before filter:", arr);

arr = arr.filter(function (num) {

	return num <= 50;

})

console.log("array after filter:", arr);


// Display Max and Min Numbers
// a- User defined function

function _MaxMin(arr) {

	var Max = arr[0];
	var Min = arr[0];

	for (var i = 0; i < arr.length; i++) {

		if (arr[i] > Max) {

			Max = arr[i];

		}

		if (arr[i] < Min) {

			Min = arr[i]
		}
	}

	console.log("Max Number:", Max);
	console.log("Min Number:", Min);
}

_MaxMin(arr);


// Display Max and Min Numbers
// b- Math functions using es6 feature (BONUS)

function MaxMin_ES6(arr) {

	Max = Math.max(...arr) // (...) is spread operator converts array to separate arguments
	Min = Math.min(...arr)
	console.log("Max Number by ES6:", Max);
	console.log("Min Number by ES6:", Min);
}

MaxMin_ES6(arr)