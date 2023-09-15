function _randomArr() {

	arr = [];
	
	for (var i = 0; arr.length < 8; i++) {

		elm = Math.floor(Math.random() * 10)

		if (elm != 0) {

			condition = true;

			for (i of arr) {

				if (elm == i) {

					condition = false;
				}
			}

			if (condition == true) {

				arr.push(elm)
			}

		}
	}

	return arr;
}

arr = _randomArr()
console.log("random array:", arr)