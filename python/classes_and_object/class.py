# Class: template for object
# Object: instance of a class
# Attributes: property, piece of data
# Methods: functionality the the object has
# Abstraction, factoring out common code - DRY, convenience, data integrity




class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return "Woof!"

    def __str__(self):
        return f"A {self.age}-year-old {self.breed} called {self.name}"

fido = Dog('Fido', 3, 'Poodle')
print(fido)
#print(fido.bark())
