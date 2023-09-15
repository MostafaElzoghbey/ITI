var students = [
  { fname: "ali", age: 22, grade: 100 },
  { fname: "nora", age: 20, grade: 90 },
  { fname: "nada", age: 25, grade: 75 },
  { fname: "heba", age: 19, grade: 50 },
  { fname: "bassem", age: 21, grade: 40 },
];

for (i = 0; i < students.length; i++) {

	window.document.write("<p><font size=\"6\"><b>" + students[i].fname + " : " + students[i].age + " : " +  students[i].grade + "</b></font></p>")
}

window.document.write("<p><font size=\"6\" color=\"red\"><b>" + "students have grade greater than 80" + "</b></font></p>")

for (i = 0; i < students.length; i++) {

	if (students[i].grade > 80) {
		
		window.document.write("<p><font size=\"6\"><b>" + students[i].fname + " : " + students[i].age + " : " +  students[i].grade + "</b></font></p>")
	}
}

window.document.write("<p><font size=\"6\" color=\"red\"><b>" + "students ordered ascending by names" + "</b></font></p>")

arr = []
for (i = 0; i < students.length; i++) {

	arr.push(students[i].fname)
}
arr.sort()

for (i = 0; i < students.length; i++) {
	
	for (j = 0; j < students.length; j++) {

		if (arr[i] == students[j].fname) {

			window.document.write("<p><font size=\"6\"><b>" + students[j].fname + " : " + students[j].age + " : " +  students[j].grade + "</b></font></p>")
		}
	}
}