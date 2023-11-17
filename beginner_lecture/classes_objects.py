# Classes are a way of creating our own data type (to model a real-world object)


# Class will define what the object is
class Student:
    # Map out attributes this object will have
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


students = {
    "Veronica": ["Information Science", 3.7, False],
    "Alexia": ["Systems Engineering", 3.7, False],
    "Valorie": ["Cybersecurity", 4.0, False],
}

attendance = []
for key, value in students.items():
    student = Student(key, value[0], value[1], value[2])
    attendance.append(student)

# A method is associated with an object while a function is not
# Below is an example
print(attendance[0].gpa, attendance[2].gpa)
print(attendance[0].on_honor_roll())

# Inheritance - define attributes and methods inside a class, then create a new class that inherits those details
# Do this by create a class with the inherited class as an argument
class InternationalStudent(Student):
    def valid_visa(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# Attributes are called without parentheses, methods are called with parentheses
test = InternationalStudent("blah", "blah", 3.5, False)
print(test.gpa, test.valid_visa())
