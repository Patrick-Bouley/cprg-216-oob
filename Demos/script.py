from students import *

s1 = Student(123, 'Sam', 3.4, 'SD', 3)
s2 = Student(124, 'Joe', 3.4, 'IT', 1)

s1.passed()

print(s1.id, s1.name, s1.gpa, s1.program, s1.semester)
print(s2.id, s2.name, s2.gpa, s2.program, s2.semester)