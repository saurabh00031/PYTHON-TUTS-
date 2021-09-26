
# *args  = not compulsory to right *args but 
#also we can write *args1,*args2,*args3


# *kwargs  = not compulsory to right *kwargs but 
#also we can write *kwargs1,*kwargs2,*kwargs3

#................................................................................

#args:-

def fun_args(*args):     #ithe tupple che form mde yete
    print(type(args))   #list becomes tupple....tupple become tupple only
    print(args[0])

sp=["saurabh","ssp","SP","patil","hang"]    #this is list
fun_args(*sp)

#.................................................................................

# *args 



def fun_args(*args):     #ithe tupple che form mde yete
    print(type(args))   #list becomes tupple....tupple become tupple only
    for item in args:
        print(item)

sp=["saurabh","ssp","SP","patil","hang"]    #this is list

fun_args(*sp) 


#..................................................................................................................

##### kwarg s######

# *args  = not compulsory to right *args but 
#also we can write *args1,*args2,*args3

def fun_args(normal,*args,**kwargs):     #ithe tupple che form mde yete function call madun
    print(type(args)) 
    print(normal)                 #list becomes tupple....tupple become tupple only
    for item in args:             #for loop for tupple
        print(item)
    for key,val in kwargs.items():
        print(key,val)
        

sp=["saurabh","ssp","SP","patil","hang"]    #this is list

normal="this is very normal" #sthis is a string      
kw={"saurabh":"monitor","ssp":"teacher","sp":"professor"}
 
fun_args(normal,*sp,**kw)


#...............................................................................................................


# *args  = not compulsory to right *args but 
#also we can write *args1,*args2,*args3

def fun_args(normal,*args,**kwargs):     #ithe tupple che form mde yete
    print(type(args)) 
    print(normal)                 #list becomes tupple....tupple become tupple only
    for item in args:             #for loop for tupple
        print(item)
    for key,val in kwargs.items():
        print(key,val)
    for key,val in kwargs.items():
        print(f"{key} is a {val}")
        

sp=["saurabh","ssp","SP","patil","hang"]    #this is list

normal="this is very normal" #sthis is a string      
kw={"saurabh":"monitor","ssp":"teacher","sp":"professor"}
 
fun_args(normal,*sp,**kw)


#..............................................................................................

def fun(norm,*args,**kwargs):
    print(type(args))
    print(type(kwargs))   #dictionary is format of qwargs 
    for item in args:
        print(item)
    print(norm)
    for key,val in kwargs.items():
        print(key,val)
    print(":finshed")
    
    
norm="this is best way"   
sp=['saurabh','ssp','ps','SP']
kw={"saurabh":"teacher","patil":"employee","ssp":"programmer"}

fun(norm,*sp,**kw)



#........................................................................................................................


def callx(key):
  return f"{key} is trying hard"


def funS(norm1,*argsSP,**kwargsSP):
    print(type(argsSP))
    print(type(kwargsSP))
    print(norm1)
    for index,item in enumerate(argsSP):
        print(index,item)
    for key,val in kwargsSP.items():
        print(key," = ",val)
        if key is 'ssp':
          print("zero")
          print(callx(key))
        else:
          print("none")
        
    
    
norm1="This is normal string"
arg1=["hi..","hello--","hey!","how r you?"]
kw1={"ssp":"SSP","sp":"SP","saurabh":"SAURABH"}


funS(norm1,*arg1,**kw1)


#....................................................................................................................