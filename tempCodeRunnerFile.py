num1=input("enter num1 ")
num2=input("enter num2 ")

try:
    num3=num1+num2
    print(num3)

except Exception as e:
    print(e*10)
    
print("plz....print this line....")