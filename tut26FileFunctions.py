
#  more about file IO............................................................................................
    

""""

f=open("harry.txt","r")               #read is default mode   ///f=open("harry.txt","r")

content=f.read(3)                     #reads first three chars
print("1",content)
        
  
content=f.read(3)                 
print("2",content)                    #reads second three chars

content=f.read(333)                   #prints till string end ....no further any printing as string is compleleted
print("3",content)

content=f.read(333)                   #kahich urla nahi print vhayla..........             
print("3",content)


                
f.close()  

"""

#......................................................................................................................


"""


f=open("harry.txt","r")   
#content=f.read()           

for line in f:                  # "it has built in \n behavior"
    print(line,end="")
                          #---------o->>>       #prints all line wise  
f.close()

f=open("harry.txt","r")   
content=f.read()   


for line in content:                        #prints char by char
    print(line,end="")

"""

#..................................................................................................................

"""
f=open("harry.txt","rt")   

print(f.readline())                                  #            ---------->>>     #"it has built in \n behavior"
print(f.readline())                                   #                 |
print(f.readline())                                    #          ------|
                  
                  #prints line by line
"""
#..................................................................................................................


"""
fp=open("harry.txt","rt")
content=fp.read()
                                      
for line in content:        #prints character by character
    print(line)

fp.close()

"""

#....................................................................................................................

"""
f=open("harry.txt","rt")   

print(f.readlines())     #-->this gives us in form of list....total complete list (list in pthon)

"""
