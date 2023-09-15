import psycopg2

connection = psycopg2.connect(host='localhost',
                              user='postgres',
                              password='sasa',
                              database='stpy')

cursor = connection.cursor()

cursor.execute('SELECT * FROM employees')

results = cursor.fetchall()

for row in results:
    
    print(f"row number {row[0]}:", row)


connection.close()
