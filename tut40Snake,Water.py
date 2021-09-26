
import random


print("Snake ......enter 1")
print("Water ......enter 2") 
print("Gun ........enter 3")

t=int(input("enter no. of rounds \n"))

while(t>0):
    ch=int(input())
    user=0
    comp=0
    cc=random.randrange(1,4)
    if ch==1 and cc==1:
        user=user
    elif ch==1 and cc==2:
        user=user+1
    elif ch==1 and cc==3:
        comp=comp+1
    elif ch==2 and cc==1:
        comp=comp+1
    elif ch==2 and cc==2:
        user=user
    elif ch==2 and cc==3:
        user=user+1    
    elif ch==3 and cc==1:
        user=user+1
    elif ch==3 and cc==2:
        comp=comp+1
    elif ch==3 and cc==3:
        user=user  
        t=t-1

if(user>comp):
    print("User won : score= ",user)
elif(user<comp):
    print("USer lose: score= ",user)
     
else:
    print("Match draw due to equal score")
 
    
     