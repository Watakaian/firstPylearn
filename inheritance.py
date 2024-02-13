# involves parent and child classes
# parent classes
class Animal:
    def speak(self):
        print("Animal  speaking")
# child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
# child class
class Cat(Dog):
    def meow(self):
        print('cat is meowing')
obj = Animal()
obj.speak()
dog=Dog()
cat=Cat()
cat.speak(),cat.meow()
