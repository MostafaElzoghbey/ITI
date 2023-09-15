-- 9.
SELECT * FROM student WHERE gender = 'male';

-- 10.
SELECT COUNT(*) FROM student WHERE gender = 'female';

-- 11.
SELECT * FROM student WHERE birth_date < '1992-10-01';

-- 12.
SELECT * FROM student WHERE birth_date <  '1991-10-01' and gender = 'male';

--13.
select cname, score from course order by score desc;

--14.
select cname, score from course order by score desc limit 1;

--15.
SELECT first_name FROM student WHERE first_name LIKE 'A%';

--16.
SELECT COUNT(*) FROM student WHERE first_name = 'Mohammed';

--17.
SELECT gender, COUNT(*) AS total_student
FROM student
GROUP BY gender;

--18.
SELECT first_name, COUNT(*) AS count FROM student GROUP BY first_name HAVING COUNT(*) > 2;

--19.
SELECT student.first_name, track.tName FROM student INNER JOIN track ON student.ID = track.ID;

--20.
SELECT student.first_name, course.score, track.tName FROM student INNER JOIN track ON student.ID = track.ID INNER JOIN course ON track.ID = course.ID;