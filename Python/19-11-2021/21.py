str=input("Enter a string:")
print("before Replacing:",str)
a=str[0]
rep=str.replace(a,'$')
string=a+rep[1:]
print("After Replacing:",string)