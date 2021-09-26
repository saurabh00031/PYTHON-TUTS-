

#...........................................................................

with open("harry.txt","r") as f:
    content=f.read()
    print(content)
    
f=open("harry.txt")
print(f.read())
f.seek(0)
print(f.read())

#..............................................................................

with open("harry.txt",'r+') as f:
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.read())
    print(f.tell())
    f.write("SSP")
    f.close()

#................................................................................

    
