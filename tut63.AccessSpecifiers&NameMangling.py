
#....................................................................................................................



                    ### if you have some data on Paper ###

                
#....................................................................................................................

               

# Public : accesible to all ....ghar ke baher kagaj chipkana...sabhi log dekh sakhenge

# Protected : sirf ghar wale dekhe kagaj ..ghar wale dekh sakhenge

# Private : room ke andar chikpayenge ...koi nahi dekhega othe than self

#...................................................................................................................


class Employee:
  x=10             #default is public ........
  _protec=12       #protected variable 
  __privt=21
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
    
  
def add(a,b):
  print("sum is : ",a+b)


harry=EmployeeXY("harry",12,"vita",10000)
harry.showDetails()

larry=EmployeeXY.fromDash("larry--11--vita--20000")
print("larry's name is",larry.name)

jerry=EmployeeXY.fromEq("jerry=13=vita=30000")
print("jerry's salary is :",jerry.salary)

harry.x=100
print("intance value of x : ",harry.x)
print("class variable value of x: ",EmployeeXY.x)

harry.changeInstance(20)
print("changed value is :-",harry.x)

harry.printStatic()
harry.Wishing()
print("sum in class is ", harry.printAdd())

add(3,4)

print(harry._protec)
print(harry._Employee__privt)   #name Mangling








#....................................................................................................................