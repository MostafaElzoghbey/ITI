from oop import *

hum1 = Human("sasa", 21, "male", "xstreet", 67408247)
print()
print(hum1.name)
print(hum1.age)
print(hum1.gender)
print(hum1.address)
print(hum1.nationnum)
hum1.health(37)
hum1.speak()
hum1.eat()
hum1.sleep()

print("#" * 30)

em = Employee(1, 'sasa', 7000)
print(em.id)
print(em.name)
em.attend("attend")
em.getSalary()
em.setSalary(1000)
Employee.employeeCount()
print()
