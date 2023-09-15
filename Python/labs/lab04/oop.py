
class Human:

    @staticmethod
    def health(tempreture):
        
        if tempreture == 37:
            
            print("Good health")  
        else:
            print("Bad health")

    def __init__(self, name, age, gender, address, nationnum):

        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.nationnum = nationnum

    def speak(self):

        print("every human can speak")
        
    def eat(self):

        print("every human should eat")

    def sleep(self):

        print("every human should sleep")


class Employee:

    count = 0

    def __init__(self, id, name, salary):

        self.id = id
        self.name = name
        self.__salary = salary

        Employee.count += 1
        
    def attend(self, attendence):
        
        self.attendence = attendence
        print(f"{self.name} is {self.attendence}")

    def setSalary(self, salary):

        if salary >= 6000 and salary <= 12000:

            self.__salary = salary
            print(self.__salary)
        else:
            print("Invalid: salary should be between 6000 and 12000")

    def getSalary(self):

        print(self.__salary)
    
    @classmethod
    def employeeCount(cls):
        
        print(Employee.count)


