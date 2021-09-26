
#..............................................................................................

#self-practicing:-

#intance and class variables
class student:
    leaves=10
    
harry=student()
larry=student()

harry.std=12
harry.marks=100
harry.leaves=10
print("leaves of harry : " ,harry.leaves)  #instances variables & cant chnage class variable

larry.std=11
larry.marks=97
larry.leaves=20
print("leaves of larry : " ,larry.leaves)  #instances variables & cant chnage class variable

print("class variable value : ", student.leaves)    


#.................................................................................................................

#..............................................................................................................

#some Concepts in python inheritance ...single inheritances


class Employee:
  leaves=10
  def __init__(self,aname,adegree,aage):
    self.name=aname
    self.degree=adegree
    self.age=aage
  
  def printdetails(self):
    print(f"this is {self.name} ....studies as {self.degree} student\n in WCE  \n is currently {self.age} years old\n")
    
  class Employee:
    leaves=11
  def __init__(self,aname,adegree,aage):
    self.name=aname
    self.degree=adegree
    self.age=aage
    
  def printdetails(self):
    print(f"this is {self.name} ....studies as {self.degree} student\n in WCE  \n is currently {self.age} years old\n")
    
  @classmethod
  def change_leaves(cls,aleaves):
    cls.leaves=aleaves
  
  @classmethod    #used as alternative constructor
  def from_dash(cls,string):
    return cls(*string.split("-"))
  
  @staticmethod
  def printplz(string):
    print("this is string printing using static method ,"+string)

class Prog(Employee): #here,i have inherited Employee class in Prog class: 
  def __init__(self,aname,adegree,aage,alang):
    self.name=aname
    self.degree=adegree
    self.age=aage
    self.lang=alang
   
  def goodDay(self):
    print(f"harry wishes you good day to {self.name}\n")  
  
  def showDetails(self):
    print(f"{self.lang}")
  
   
   
   
   
harry=Employee("saurabh","CS","21")
larry=Employee("patil","IT","20")
karan=Employee.from_dash("Karan-ENTC-24")


ssp=Prog("saurabhP","CS","20",[[1,2],[3,4],[5,6]])


karan.printplz("Saurabh")     
                                 #this both r possible here.......
Employee.printplz("Saurabh")

harry.leaves=11
harry.change_leaves(8)
print(harry.leaves)

#harry.goodDay()
ssp.showDetails()



#.................................................................................................................................










#.......................................................................................................................