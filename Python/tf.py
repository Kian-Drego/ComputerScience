class student:
    def __init__(self, name, dob, marks):
        self.name = name
        self.dob = dob
        self.marks = marks

    def displayExamMark(self):
        return self.marks

class fullTimeStudent(student):
    pass

myStudent = fullTimeStudent("Kian", "11-02-09", 99)
print(myStudent.displayExamMark())
