# *********************************** CLASS METHOD **********************************************

# classmethod() is a function that returns a method of a class and we also have @classmethod() decorator
# classmethod can be called  by both instance and class itself

from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name,date.today().year - year)

	
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)


