
class Student:
    
    def __init__(self, name, majors, year):
        assert isinstance(name, str), "name must be a string!"
        assert isinstance(majors, list) and all([isinstance(m,str) for m in majors]),\
            "majors must be a list of strings!"
        
        self.name = name
        self.majors = majors
        self.year = year
        
    def num_majors(self):
        return self.name
        
    def __repr__(self):
        return "Student: {}".format(self.name)