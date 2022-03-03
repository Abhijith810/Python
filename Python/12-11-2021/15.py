num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
n=input("enter the operator:")
if(n=="+"):
    c=num1+num2
    print("sum of",num1,"and",num2,"is:",c)
elif(n=="-"):
    if(num1>num2):
        c=num1-num2
        print("difference between",num1,"and",num2,"is:",c)
    else:
        c=num2-num1
        print("difference between",num2,"and",num1,"is:",c)
elif(n=="*"):
    c=num1*num2
    print("product of",num1,"and",num2,"is:",c)
elif(n=="/"):
    c=num1/num2;
    print("division of",num1,"and",num2,"is:",c)
else:
    print("invalid")