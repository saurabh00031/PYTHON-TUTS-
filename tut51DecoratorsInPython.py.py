
#........

def function1():
    print("i m python pro")
    
func2=function1

del function1

func2()  # #still #OUTPUT : -- i m python pro       


#........................................................................................................

#some basics

def funcret(num):
    if num==0:
        return print 
    if num==1:
        return int 
    else:
        return sum

for i in range(4):
    print(funcret(i))


def show(func):
    func("saurabh")
    
show(print) 

#...................................................................................................................

#decorators:::-

#decorators in python:-

def dec1(func1):
    def show():
        print("show it")
        func1()
        print("showed successfully")
    return show 

def harry():
    print("harry is star") 
    
harry=dec1(harry) 
harry()

#................................................

#decorators in python:-

def dec1(func1):
    def show():
        print("show it")
        func1()
        print("showed successfully")
    return show 

@dec1
def harry():
    print("harry is star") 
    
#harry=dec1(harry) 

harry()
 

#....................................................................................................



#$$$practicing

def decoratorX(str):
  print("decoratorX")
  return str
  
def decoratorY(str):
  print("decoratorY")
  return str

@decoratorX
@decoratorY
def calling1():
  print("i m calling function1")
  

def calling2():
  print("i m calling function2")
  
calling1()

#....................................................................................................




