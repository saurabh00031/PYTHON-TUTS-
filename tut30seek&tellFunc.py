#............................................................................................................

f=open("harry.txt","r")
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())
f.close()

#...............................................................................................................