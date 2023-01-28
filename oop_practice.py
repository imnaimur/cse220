# class Course():
#     def __init__(self,dept,fac=None,sec= None) -> None:
#         self.dept = dept
#         pass
#     def __add__(self,other):
#         self.sum = self.dept + other.dept
#         return self.sum
# num1 = Course(10)
# num2 = Course(30)
# print(num1+ num2)




# # c1 = Course("CSE110", "TBA", 8)
# # c1.detail()
# # print("===============")
# # c2 = Course("CSE111", "TBA", 9)
# # c2.detail()
class Student:
    id = 0
    def __init__(self,name,dept,age,cg) -> None:
        Student.id +=1
        self.name = name
        self.age = age
        self.dept = dept
        self.cg = cg

    @classmethod
    def from_String(cls,string):
        string = string.split("-")
        i,j,k,l = tuple(string)
        return Student(i,j,k,l)
    def get_details(self):
        print("ID:", Student.id)
        print("Name:",self.name)
        print("Department:",self.dept)
        print("Age:", self.age)
        print("CGPA:", self.cg)
    

s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()