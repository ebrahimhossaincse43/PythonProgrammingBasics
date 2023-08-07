class Person:
    def __init__(self, name, age):  # Constructor to initialize name and age attributes
        self.name = name
        self.age = age

    def say_hello(self):  # Method to greet and introduce the person
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):  # Student class inherits from Person class
    def __init__(self, name, age, grade):  # Constructor to initialize name, age, and grade attributes
        super().__init__(name, age)  # Call the parent class constructor to initialize name and age
        self.grade = grade  # Additional attribute specific to the Student class

    def say_hello(self):  # Override the say_hello method of the parent class
        super().say_hello()  # Call the parent class say_hello method to introduce the student as a person
        print(f"I am a student in grade {self.grade}.")  # Print additional information specific to the Student class

# Creating an instance of the base class
# person = Person("John", 30)
# person.say_hello()

# Creating an instance of the derived class
student = Student("Mary", 18, 12)
student.say_hello()
