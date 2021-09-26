
#...............................................................................................................


#map,filter and reduce

from functools import reduce
import time 
list1=[1,2,3,4,5,6,7,9,8]

#map
for item in list1:
  val=list(map(lambda item:item*item,list1))
print(val)

def greater_than_5(num):
  return num>5

#filter
for item in list1:
  val=list(filter(greater_than_5,list1))
print(val)

#reduce


valx=reduce(lambda x,y:x+y,list1)
print(valx)





#without map,simply ...we do....#.........................................................................

#.................................................................................

numbers=["3","4","5","6","7"]

for i in range(len(numbers)):
    numbers[i]=int(numbers[i])+1

print(numbers[0])

#...................................................................................

#Map:-
#square of numbers
numbers=["3","4","5","6","7"]

numbers=list(map(int,numbers))

print(numbers[0])

#..........................................................................................

numbers=["3","4","5","6","7"]
numbers=list(map(int,numbers))
print(numbers[0])



def sq(numx):
    return numx*numx
 
num=[1,2,3,4,5]    
square=list(map(sq,num))
print(square)

#.................................................................................................................

numbers=["3","4","5","6","7"]
numbers=list(map(int,numbers))
print(numbers[0])




 
num=[1,2,3,4,5]    
square=list(map(lambda x:x*x,num))
print(square)


#...................................................................................................................

def square(a):
    return a*a 
    
def cube(a):
    return a*a*a 
    
func=[square,cube]
num=[2,3,4,5,6,7]

for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val) 


#......................................................................................................................

#filter:-


list2=[1,2,3,4,5,6,7,8,9,0]
 
def is_greater_than_5(n):
    return n>5
    

greater_than_5_obj=filter(is_greater_than_5,list2)

x=list(greater_than_5_obj)
print(x) 

#..................................................................................................................

#reduce:

from functools import reduce
list1=[1,2,3,4,5,6,7]
sum=0
for i in list1:
	sum=sum+i
print(sum)

num=reduce(lambda x,y:x+y,list1)
print(num)

#...................................................................................................................


#practiced........................................

list1=["1","2","3","4","5"]
print(list(map(int,list1)))

def cb(num):
    return num*num*num 
    
def sqr(num):
    return num*num

powFour=lambda x:x*x*x*x

list2=[1,2,3,4,5]
print(list(map(cb,list2)))
print(list(map(sqr,list2)))
print(list(map(powFour,list2))) 



#........................................................................................................
def sqr(num):
  print(num*num,end=" ")
  
def cb(num):
  print(num*num*num)
  
func_grp=[sqr,cb]
list1=[1,2,4,7,9]
list2=[4,5,6,7,0,8]

for item in list1:
  valx=list(map(lambda x:x(item),func_grp))
  
  
list3=[list1,list2]

for index,item in enumerate(list1):
  val=list(map(lambda x:x(item),func_grp))

#................................................................................................................

#practicing

#................................................................................................................

def square(a):
    return a*a 
    
def cube(a):
    return a*a*a 
    
def powk(a):
    return a*a*a*a
    
func=[square,cube,powk]
num=[2,3,4,5,6,7]

for i in num:
    val=list(map(lambda x:x(i),func))
    print(val)
    
    


#...............................................................................................................
