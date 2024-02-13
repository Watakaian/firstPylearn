'''
Class is a blueprint of an object
#An object is an instance of a class
'''


class Person:
    # properties/attributes/characteristics --> attributes(variables) and behaviours(methods(functions))
    name = 'Bob'
    age = 23
    location = 'Westlands'
    # method
    def speak(self):
        print('Person is speaking')
accountant = Person() #instantiating an object
print(accountant.name)
accountant.speak()