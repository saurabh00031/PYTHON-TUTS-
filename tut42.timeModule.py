
#................................................................................................................

#checking while and for loop execution time using imported time module......


import time

initial=time.time()


for i in range(45):
    print(i,end=" ")
    
print(time.time()-initial)  
initial2=time.time()

print("")   

k=0
while(k<45):
    print(k,end=" ")
    k=k+1
    
print(time.time()-initial2)    

#...............................................................................................

import time


localtime=time.asctime(time.localtime(time.time()))
print(localtime)

#...................................................................................................

#delays in printing as output......

import time

i=0
while i<10:
  print(i)
  i=i+1
  time.sleep(1)


#.....................................................................................................

#some practices........

import time 
initial1=time.time()

i=0
while i<=10:
  print(i,end=" ")
  i=i+1
x=time.time()
initial2= time.time()-initial1 
print(initial2)

print("\n")
for i in range(11):
  print(i,end=" ")
print(time.time()-x)