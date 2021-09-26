
#...................................................................................................................

#self in python:-

class Employee:
    no_of_leaves=8
    
    def printdetails(self):
      return f"Name is {self.name} salary is {self.salary}  "


harry=Employee()
larry=Employee() 

harry.name="harry patil"
harry.salary=10000
harry.role="instructor"

larry.name="larry patil"
harry.salary=20000
harry.role="sub-instructor"

print(harry.printdetails())




#.....................................................................................................................

#int _it:-

class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
      self.name=aname
      self.salary=asalary
      self.role=arole
      
    def printx(self):
      print(self.name)
      
   
    
    


harry=Employee("harry patil",10000,"instructor")

print(harry.salary)
harry.printx()


#...............................................................................................................


#self practicing:-

class Employee:
  def __init__(self,aname,adegree,aage):
    self.name=aname
    self.degree=adegree
    self.age=aage
    
  def printdetails(self):
    print(f"this is {self.name} ....studies as {self.degree} student\n in WCE  \n is currently {self.age} years old\n")
    

harry=Employee("saurabh","CS","21")
harry.printdetails()

#...............................................................................................................

class Employee:
  leaves=10
  def __init__(self,aname,adegree,aage):
    self.name=aname
    self.degree=adegree
    self.age=aage
    
  def printdetails(self):
    print(f"this is {self.name} ....studies as {self.degree} student\n in WCE  \n is currently {self.age} years old\n")
    
 
    
   
harry=Employee("saurabh","CS","21")
harry.printdetails()

larry=Employee("patil","IT","20")
larry.printdetails()

Employee.leaves=100
print("class variable : ",Employee.leaves)
harry.leaves=10
print("instance variable: ",harry.leaves)





#..................................................................................................................


