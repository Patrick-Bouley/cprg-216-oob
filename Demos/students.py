class Student:
    def __init__(self, id, name, gpa, program, semester):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.program = program
        self.semester = semester

    def passed(self):
        self.semester += 1
        