class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#Implementing a method called introduce that prints a message introducing the person with their name, age, and gender.
    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} and I am {self.gender}")       


# Create an instance of the Person class
person1 = Person("David", 28, "male")

#Calling the introduce method to display the person's information.
person1.introduce()