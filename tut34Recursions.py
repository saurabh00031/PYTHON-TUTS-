#///////////////////////////////

def fact(n):
    if n==1:
        return 1 
    elif n==0:
        return 1 
    else:
        return n*fact(n-1)


num=int(input())

print( fact(num) )

#/////////////////////////////////

def fibbo(n):
    if n==1:
        return 0 
    elif n==2:
        return 1 
    else:
        return fibbo(n-1)+fibbo(n-2)


num=int(input())

print( fibbo(num) )


