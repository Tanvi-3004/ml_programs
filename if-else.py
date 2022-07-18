# maximum of two numbers

a=int(input("a:"))
b=int(input("b:"))
if a>b:
    print("a is greater")
else:
    print("b is greater")


# odd/even number

c=int(input("c:"))
if c%2==0:
    print("number is even")
else:
    print("number is odd")

# 10% discount if bill amount greater than 5000 otherwisw 5% discount

bamt=int(input("bill amount:"))
if bamt>5000:
    dis=0.10*bamt
else:
    dis=0.05*bamt
nbill=bamt-dis
print("discount",dis)
print("net bill",nbill)

# given number is postive, negative or zero


n=int(input("n:"))
if n>0:
    print("number is positive")
elif n<0:
    print("number is negative")
else:
    print("number is zero")

# highest of three numbers

d=int(input("D:"))
e=int(input("E:"))
f=int(input("F:"))
if d>e and d>f:
    print("d is greater")
elif e>f:
    print("e is greater")
else:
    print("f is greater")





    
    
