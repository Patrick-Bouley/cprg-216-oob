class Student:

    def _init__(self, name_val, ID_val, sem_val, gpa_val):
        self.Name = name_val
        self.id = ID_val
        self.semester = sem_val
        self.gpa = gpa_val

    def set_name(self,value):
        self.Name = value

    def set_id(self,value):
        self.id = value
    
    def set_semester(self,value):
        self.semester = value

    def set_gpa(self,value):
        self.gpa = value