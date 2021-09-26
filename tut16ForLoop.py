
#for loop in python
print(".................................................................")
#.................................................................................................................
list1=[1,2,3]

for item in list1:        #for loop for lists
    print(item)
print(".................................................................")
#..................................................................................................................

list2=[["ssp",1],["saurabh",2],["sp",3],["patil",4]]

for item,lollipop in list2:        #for loop for lists of list
    print(item,lollipop)

#...................................................................................................................

dict1=dict(list2)           #list typecasted to dictionary...........
print(dict1)                #print dictionary 
print(".................................................................")
for item,lollipop in dict1.items():        #for loop  for dictionary
    print(item,lollipop)                   #

print(".................................................................")
for item in dict1:          #keys for dictionary      
    print(item)


#.......................................................................................................
print(".....................................................................................................")
items=[int,float,"string",1,2,"sp"]

for item in items:
    if str(item).isnumeric() and item>1:
        print(item) 
   
print(".....................................................................................................")




#.......................................................................................................................

#$.......practiced...........#$

list1=[12,2,3,44]
list2=[1,2,3,4]
list3=[11,22,33,44]

list4=[list1,list2,list3]


for index,item  in enumerate(list4):
  print(index,item)
   
dict1=dict(zip(list1,list2))
print(dict1) 

dict2=dict(zip(list1,list4))
print(dict2)

for key,val in dict2.items():
  print(key,val[0],val[1],val[2])


#....................................................................................................................

#practicing::::-

list1=[1,2,3,4,5,6,7]
list2=[11,22,33,44,55,66]
list3=[list1,list2]
print("......................................................................")
print(list3)
print("......................................................................")
for item in list3:
    print(item[0])
print("......................................................................")   
for index,item in enumerate(list1):
    print(index,item)
print("......................................................................")

dict1=dict(zip(list1,list2))

x=dict1.get(2)
print(x)

print("......................................................................")

for key,val in dict1.items():
    print(key," = ",val)
    
print("......................................................................") 

dict2=dict(zip(list1,list3))
print(dict2)


for key,val in dict2.items():
    print(key," = ",val[0],val[1],val[2],val[3])

print("......................................................................") 

tp=tuple(list1)
print(tp)

lt=list(tp)
print(lt)

print("......................................................................") 

list4=[list3,list3]
print(list4)

print("......................................................................") 

for item in list4:
    print(item[0][0],item[0][1],item[0][2])

print("......................................................................") 



listx=[]
print("enter numbers")


n = int(input("Enter number of elements : ")) 
  
# Below line read inputs from user using map() function  
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
  
#print(a)

for item in a:
    print(item)



#....................................................................................................................

#self-practice:-



n=int(input())
a=list(map(int,input().strip().split() ))[:n]
print(a)

list1=[1,2,3,4,5]
list2=[10,20,30,40,50]
list3=[list1,list2]
list4=[list3,list3]

for index,item in enumerate(list3):
  print(item[0],item[1])
  
print(list4)

for index,item in enumerate(list4):
  print(item[0])

dict1=dict(zip(list1,list4))
print(dict1)
for key,val in dict1.items():
  print(key," = ",val[0][0],val[0][1])

listx=[1,2,3,4,5,6]
listy=[11,22,33,44,55,66,77]
print(dict(zip(listx,listy)))
print(dict1.get(1))


#...................................................................................................................