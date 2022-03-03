dict1={'fruit': 'apple','price': '100'}
dict2={'fruit': 'Mango','price': '200'}
print("dictionary 1:",dict1)
print("dictionary 2:",dict2)
d=dict1.copy()
d.update(dict2)
print(d)