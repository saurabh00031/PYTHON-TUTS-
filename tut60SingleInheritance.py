
#...............................................................................................................

#INHERITANCE:-

#...............................................................................................................

# inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are: 
# It represents real-world relationships well.
# It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
# Below is a simple example of inheritance in Python 


#..................................................................................................................



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

   
harry=Prog("saurabh","CS","21")
larry=Prog("patil","IT","20")
karan=Prog.from_dash("Karan-ENTC-24")



karan.printplz("Saurabh")     
                                 #this both r possible here.......
Employee.printplz("Saurabh")

harry.leaves=11
harry.change_leaves(8)
print(harry.leaves)

harry.goodDay()











#......................................................................................................................