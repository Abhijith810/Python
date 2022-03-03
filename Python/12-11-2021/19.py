n=int(input("enter the final year:"))
for num in range(2021,n):
    if(num%4==0 or num%100==0 or num%400==0):
        print(num)