class Student:
    def __init__(self,name,student_id, email, age,department, practical_mark, viva_mark):
        self.name=name
        self.student_id=student_id
        self._email=email
        self.age=age
        self.department=department
        self.practical_mark = practical_mark
        self.viva_mark = viva_mark
    def display_info(self):
        print("Name:",self.name)
        print("Student Id:",self.student_id)
        print("Email:",self._email)
        print("Age:",self.age)
        print("Department:",self.department)
    # def calculate_result(self, *marks): 
    def calculate_result(self):

        print(f"Result = {int(self.practical_mark)+ int(self.viva_mark)}")
        
        
        
    
    def get_student_type(self):
        return "Student type unknow"

class UndergraduateStudent(Student):
    def __init__(self,name,student_id, email, age,department,practical_mark, viva_mark, semester):
        super().__init__(name,student_id, email, age, department, practical_mark, viva_mark)
        self.semester=semester
    def display_info(self):
        super().display_info()  
        print("Semester:",self.semester)

    def get_student_type(self):
        return "UnderGraduate Student"

    
class GraduateStudent(Student):  
    def __init__(self,name,student_id, email, age,department, practical_mark, viva_mark, research_topic):
            super().__init__(name,student_id, email, age,department, practical_mark, viva_mark)
            self.research_topic=research_topic
    def display_info(self):
            super().display_info()  
            print("Research_topic:",self.research_topic)
    def get_student_type(self):
            return "Graduate Student"


student1 = UndergraduateStudent(
    "Karim", 102, "karim@gmail.com",
    21, "CSE", 23, 54, 3
)
student2= GraduateStudent(
    "Anika", 103, "anika@gmail.com",
    24, "CSE", 21, 65, "NLP"
)
print("\nStudent Management System")
print("\n---Student1---")
student1.display_info()
student1.calculate_result()
print(student1.get_student_type())
print("\n---Student2---")
student2.display_info()
student2.calculate_result()
print(student2.get_student_type())





