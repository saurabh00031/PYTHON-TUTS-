
#...........................................................................................................

a="harry,"
b=100
c="this is new style {} {}"
d=c.format(a,b)
print(d)

#.............................................................................................................

a="harry,"
b=100
c="this is new style {0} {1}"
d=c.format(a,b)
print(d) 

#................................................................................................................

a="harry,"
b=100
c="this is new style {1} {0}"       
d=c.format(a,b)
print(d)

#...................................................................................................................

a="harry,"
b=100

c=f"this is new style {a} {b} {7*6} "

print(c) 

#..................................................................................................................

import math

a="harry,"
b=100

c=f"this is new style {a} {b} {7*6} {math.cos(3.14)} "

print(c)
#..........................................................................................................................

#some practice..

sp1="saurabh is good"
sp2="saurabh is bad"

print(f"this are statements:1){sp1} & 2){sp2}\n ")

list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[list1,list2]

#.........................................................................................................................