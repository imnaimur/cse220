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
# class Student:
#     id = 0
#     def __init__(self,name,dept,age,cg) -> None:
#         Student.id +=1
#         self.name = name
#         self.age = age
#         self.dept = dept
#         self.cg = cg

#     @classmethod
#     def from_String(cls,string):
#         string = string.split("-")
#         i,j,k,l = tuple(string)
#         return Student(i,j,k,l)
#     def get_details(self):
#         print("ID:", Student.id)
#         print("Name:",self.name)
#         print("Department:",self.dept)
#         print("Age:", self.age)
#         print("CGPA:", self.cg)
    

# s1 = Student("Samin", "CSE", 21, 3.91)
# s1.get_details()
# print("-----------------------")
# s2 = Student("Fahim", "ECE", 21, 3.85)
# s2.get_details()
# print("-----------------------")
# s3 = Student("Tahura", "EEE", 22, 3.01)
# s3.get_details()
# print("-----------------------")
# s4 = Student.from_String("Sumaiya-BBA-23-3.96")
# s4.get_details()

# class Assassin:
#     total = 0
#     def __init__(self,name,rate) -> None:
#         Assassin.total += 1
#         self.name = name
#         self.rate = rate
    
#     @classmethod
#     def failureRate(cls,name,rate):
#         sub = 100 - rate
#         return Assassin(name,sub)
#     @classmethod
#     def failurePercentage(cls,name,rate):
#         sub = 100 - int(rate[:-1:])
#         return Assassin(name,sub)
#     def printDetails(self):
#         print("Name:",self.name)
#         print(f"Success rate: {self.rate}%")
#         print("Total number of Assassin", Assassin.total)

# john_wick = Assassin('John Wick', 100)
# john_wick.printDetails()
# print('================================')
# nagisa = Assassin.failureRate("Nagisa", 20)
# nagisa.printDetails()
# print('================================')
# akabane = Assassin.failurePercentage("Akabane", "10%")
# akabane.printDetails()

# class Passenger:
#     count = 0
#     def __init__(self,name) -> None:
#         Passenger.count += 1
#         self.name = name
#     def set_bag_weight(self,w):
#         if(w>50):
#             ext_f = 100
#         elif(20<w<51):
#             ext_f = 50
#         else:
#             ext_f = 0
#         self.total = 450 + ext_f
#     def printDetail(self):
#         print("Name: ", self.name)
#         print("Bus Fare:", self.total)


# print("Total Passenger:", Passenger.count) 
# p1 = Passenger("Jack") 
# p1.set_bag_weight(90) 
# p2 = Passenger("Carol") 
# p2.set_bag_weight(10) 
# p3 = Passenger("Mike") 
# p3.set_bag_weight(25) 
# print("=========================") 
# p1.printDetail() 
# print("=========================") 
# p2.printDetail() 
# print("=========================") 
# p3.printDetail() 
# print("=========================") 
# print("Total Passenger:", Passenger.count)


class Travel:
    count = 0
    def __init__(self,source,destination) -> None:
        Travel.count += 1
        self.s = source
        self.d = destination
        self.h = 1
    def set_time(self,h):
        self.h = h
    def display_travel_info(self):
        return f"Source: {self.s}\nDestination: {self.d}\nFlight time: {self.h}.00"
    def set_source(self,s):
        self.s = s
    def set_destination(self,d):
        self.d = d


print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)