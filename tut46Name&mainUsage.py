#main.py---------->


#import sklearn

def printhar(string):
    return "give this string ",string
     
def add(num1,num2):
    return num1+num2+10

if __name__=='__main__' :
    print(printhar("harry1"))
    print(add(10,20))


#main2.py---------->

import main 

print(main.add(6,7))