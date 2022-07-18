#user defined function

def add(x,y):
    ans=x+y
    print("addition is",ans)
a=int(input("enter a:"))
b=int(input("enter b:"))
add(a,b)


def max(x,y):
    if x>y:
        return x
    else:
        return y
c=int(input("enter c:"))
d=int(input("enter d:"))
ans=max(c,d)
print("max no. is::",ans)

def fact(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans
m=int(input("enter m:"))
b=fact(m)
print("factorial of m is  ",b)

