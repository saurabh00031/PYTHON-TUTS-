
#.....................................................................................................................
                                            # ---------------- # 
                                            #  CLASSMETHODS    #
                                            # ---------------- #
#.....................................................................................................................
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
  
    
harry=Employee("saurabh","CS","21")
harry.printdetails()

larry=Employee("patil","IT","20")
larry.printdetails()

Employee.leaves=100
print("class variable : ",Employee.leaves)
harry.leaves=10
print("instance variable: ",harry.leaves)

    
   
harry=Employee("saurabh","CS","21")
harry.printdetails()
harry.change_leaves(8)

print(harry.leaves)





#...................................................................................................................