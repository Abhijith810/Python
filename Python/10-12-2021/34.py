str=input("Enter a string:")
def fun(str1):
    if str[-3:]!='ing':
        print(str+"ing")
    else:
        print(str + "ly")
fun(str)

