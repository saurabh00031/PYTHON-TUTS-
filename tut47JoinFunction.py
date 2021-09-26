
#...commonly can be joined ...............

list1=["John","Cena","Randy","Orton","Khali","Jinder","Mahal"]


a=" and ".join(list1)
print(a,"-- other wwe superstars")

b=" or ".join(list1)
print(b,"-- other wwe superstars")

c=" , ".join(list1)
print(c,"-- other wwe superstars")

#...........................................................

'''
OUTPUT:

John and Cena and Randy and Orton and Khali and Jinder and Mahal -- other wwe superstars
John or Cena or Randy or Orton or Khali or Jinder or Mahal -- other wwe superstars
John , Cena , Randy , Orton , Khali , Jinder , Mahal -- other wwe superstars

'''


#...............................................................................................................

list1=["saurabh","ssp","patil"]

x=" and ".join(list1)
print(x)

x=" or  ".join(list1)
print(x)

x=" ,  ".join(list1)
print(x) 

#..............................................................................................................