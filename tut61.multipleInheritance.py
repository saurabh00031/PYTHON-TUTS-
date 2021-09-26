
#.......................................................................................................................


class Employee:
  x=10
  l=10
  y=50
  def __init__(self,a,b,c,d):
    self.name=a 
    self.std=b 
    self.city=c 
    self.salary=d 
    
  def showDetails(self):
    print(f"name is {self.name}\n std is {self.std}\n city is {self.city}\n salary is {self.salary}\n")
   
  @classmethod
  def changeInstance(cls,d):
    cls.x=d 
    
  @classmethod
  def fromDash(cls,string):
    return cls(*string.split("--"))
  
  @classmethod
  def fromEq(cls,string):
    sp=string.split("=")
    return cls(sp[0],sp[1],sp[2],sp[3])
    
  @staticmethod
  def printStatic():
    print("print static plxz")
    
class EmployeeX:
  z=100
  def Wishing(self):
    print("harry wishes you happy coding\n")


class EmployeeXY(Employee,EmployeeX):
  def printAdd(self):
    return self.l+self.z
    
  
   


harry=EmployeeXY("harry",12,"vita",10000)
harry.showDetails()

larry=EmployeeXY.fromDash("larry--11--vita--20000")
print("larry's name is",larry.name)

jerry=EmployeeXY.fromEq("jerry=13=vita=30000")
print("jerry's salary is :",jerry.salary)

harry.x=100
print(harry.x)
print(EmployeeXY.x)

harry.changeInstance(20)
print("changed value is :-",harry.x)

harry.printStatic()
harry.Wishing()
print(harry.printAdd())







#..........................................................................................................................