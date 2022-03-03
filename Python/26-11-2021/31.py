n=int(input("Enter the limit:"))
l=[]
print("Enter the values:")
for i in range(0,n):
    m=int(input())
    l.append(m)
print("list is:",l)
s=0
for i in l:
    s=s+i
print("sum of list is:",s)
