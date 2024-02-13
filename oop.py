class Person:
    def __init__(self,firstName,age,gender):
        self.firstName = firstName
        self.age = age
        self.gender = gender
    def details(self):
        print(self.firstName,'is studying')
teacher=Person('Joe',56,'male')
accountant=Person('Mary',21,'female')
doctor=Person('John',34,'male')
print('My name is',teacher.firstName,'and I am',teacher.age,'years old','and my gender is',teacher.gender)
print(doctor.details())
