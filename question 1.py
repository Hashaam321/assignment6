class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
student1 = Student("Hashaam", 20, "S12345", "Computer Science")
print("Student Information:")
student1.display_student_info()
