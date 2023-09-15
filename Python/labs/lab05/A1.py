class Animal:
    
    def __init__(self, kind, color, age):
        
        self.kind = kind
        self.color = color
        self.age = age

    def eat(self):
        
        print(f"{self.kind} is eating.")

    def sleep(self):
        
        print(f"{self.kind} is sleeping.")

    def walk(self):
        
        print(f"{self.kind} is walking.")

    def run(self):
        
        print(f"{self.kind} is running.")

class Cat(Animal):
    
    def __init__(self, kind, color, age, whisker):
        
        super().__init__(kind, color, age)
        self.has_whisker = whisker

    def eat(self):
        
        print(f"{self.kind} is eating cat food like milk.")

    def sound(self):
        
        print(f"{self.kind} is meowing.")

    def scratch(self):
        
        print(f"{self.kind} is scratching.")


cat = Cat("cat", "White", 2, "has whisker")
print()
print(cat.kind)
print(cat.color)
print(cat.age, "month")
print(cat.has_whisker)
cat.eat()
cat.sound()
cat.scratch()
cat.sleep()
cat.run()
print()