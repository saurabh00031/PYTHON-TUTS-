
#....................................................................................................................
#multiple inheritance


  
  
class Employee:
  leaves=10
  def __init__(self,aname,adegree,aage):
    self.name=aname
    self.degree=adegree
    self.age=aage
    
  def __init__(self):
    pass
    
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

class Prog(Employee): #here,i have inherited Employee class in Prog class
  def goodDay(self):
    print("harry wishes you good day\n")  
    
class ProgPRO(Prog,Multi):
  def add(self,a,b,c):
    self.first=a 
    self.second=b 
    self.third=c
    print("first string is ",self.first)
    print("second string is ",self.second)
    print("third string is ",self.third)

   
harry=ProgPRO("saurabh","CS","21")
larry=ProgPRO("patil","IT","20")
karan=ProgPRO.from_dash("Karan-ENTC-24")



karan.printplz("Saurabh")     
                                 #this both r possible here.......
Employee.printplz("Saurabh")

harry.leaves=11
harry.change_leaves(8)
print(harry.leaves)

harry.goodDay()



#....................................................................................................................