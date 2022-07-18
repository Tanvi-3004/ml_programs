L=[]
count=0
n=int(input("enter the number of elements in the list:"))
for i in range(0,n):
    L.append(input("enter the item:"))
for j in L:
    print("tuple1[%d] = %s"%(count, j))
    count = count+1
    

