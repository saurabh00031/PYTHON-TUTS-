def add(a,b):
    return a+b 
    
minus=lambda x,y:x-y
print(add(1,2),minus(3,4))    #output : 3 -1

#..........................................................................
#sorting with respect to first element 

def list1_first(list1):
    return list1[0]

list1=[[111,9],[9,6],[8,34]]
list1.sort(key=list1_first)
print(list1)

    #........
list1=[[111,9],[9,6],[8,34]]
list1.sort(key=lambda x:x[0])

#..........................................................................
#sorting with respect to first element 

def list1_first(list1):
    return list1[1]

list1=[[111,9],[9,6],[8,34]]
list1.sort(key=list1_first)
print(list1)

   #........

list1=[[111,9],[9,6],[8,34]]
list1.sort(key=lambda x:x[1])


print(list1)

#...................................................................................
#sorting with respect to second element 

# some self practiced 

#lambda functions

def sq(num):
  return num*num 
  
def cb(num):
  return num*num*num 
  
def powFour(num):
  return num*num*num*num 
ssp=lambda x:x*x

numx=4
print(sq(numx))
print(cb(numx))
print(powFour(numx))
print(ssp(numx))

#.................................................................................................................


def add(x,y):
    return x+y

subtract=lambda x,y:x-y


numx=10
numy=11
print(add(numx,numy))
print(subtract(numx,numy))
print((lambda x,y:x*y)(numx,numy) )
print((lambda x,y:x/y)(numx,numy) )
print((lambda x,y:x**y)(numx,numy) )


#.................................................................................................................