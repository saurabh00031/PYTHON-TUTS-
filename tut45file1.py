#.......................................................................................................

import sys
print(sys.path)
print("helo")   

import tut45file2     #direct access is not possible
tut45file2.a
print(tut45file2.a)

from tut45file2 import a   #direct access is possible
print(a)

tut45file2.printjoke("pass the joke to file2 of tut 45 : ")
#............................................................................................................








#practiced>>>>>>>>>

#main:------------------------------------------------------------
def add(a,b):
    return a+b 
def saurabh(string):
     return string
     
     
     
import main1
print(add(main1.a,main1.b))

from main1 import string as str
print(saurabh(str))
print(main1.big(10))
    
#main1:------------------------------------------------------------------
a=10
b=20
string="this is saurabh"    
def big(num):
   return num*10


#..........................................................................