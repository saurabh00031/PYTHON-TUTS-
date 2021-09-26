
#...........................................................................................................

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
    
harry=Employee("saurabh","CS","21")
larry=Employee("patil","IT","20")
karan=Employee.from_dash("Karan-ENTC-24")

karan.printplz("Saurabh")     
                                 #this both r possible here.......
Employee.printplz("Saurabh")

harry.leaves=11
harry.change_leaves(8)
print(harry.leaves)











#..............................................................................................................