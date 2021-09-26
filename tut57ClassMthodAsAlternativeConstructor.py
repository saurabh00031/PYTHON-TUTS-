
#....................................................................................................................

#class method can be used as alternative constructor and it will be helful as if only string is passed 
# we cam fetch data in sequence manner


class Employee:
  leaves=10
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
  def from_str(cls,string):
    params=string.split("-")
    return cls(params[0],params[1],params[2])
  
  
   
   
harry=Employee("saurabh","CS","21")
harry.printdetails()

larry=Employee("patil","IT","20")
larry.printdetails()

karan=Employee.from_str("Karan-ENTC-24")
print(karan.degree)

Employee.leaves=100
print("class variable : ",Employee.leaves)
harry.leaves=10
print("instance variable: ",harry.leaves)

    
   
harry=Employee("saurabh","CS","21")
harry.printdetails()
harry.change_leaves(8)

print(harry.leaves)



#....................................................................................................................


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
  def from_str(cls,string):
    return cls(*string.split("-"))
  
  
   
   
harry=Employee("saurabh","CS","21")
harry.printdetails()

larry=Employee("patil","IT","20")
larry.printdetails()

karan=Employee.from_str("Karan-ENTC-24")
print(karan.degree)

Employee.leaves=100
print("class variable : ",Employee.leaves)
harry.leaves=10
print("instance variable: ",harry.leaves)

    
   
harry=Employee("saurabh","CS","21")
harry.printdetails()
harry.change_leaves(8)

print(harry.leaves)






 


#....................................................................................................................

#practicing



class Employee:
  x=10
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
  
harry=Employee("harry",12,"vita",10000)
harry.showDetails()

larry=Employee.fromDash("larry--11--vita--20000")
print("larry's name is ",larry.name)

jerry=Employee.fromEq("jerry=13=vita=30000")
print("jerry's salary is :  ",jerry.salary)

harry.x=100
print(harry.x)
print(Employee.x)

harry.changeInstance(20)
print("changed value is :-",harry.x)







#....................................................................................................................
