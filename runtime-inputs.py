'''a = input("enter data:")
b = input("enter data:")
print(a+b)'''

'''a,b = input("enter the names:").split(",")
print(a+b)'''

'''a,b = [x for x in input("enter the names:").split(",")]
print(a+b)'''

'''a = int(input("a value:"))
b = int(input("b value:"))
print(a+b)'''

'''a,b = int(input("enter the values:")).split(",")
print(a+b)''' #ValueError: invalid literal for int() with base 10: '9,11'
        
'''a,b = [int(x) for x in input("enter the values:").split(",")]
print(a+b)'''

'''a,b = map(int, input("enter the values:").split(","))
print(a+b)'''

'''a,b = list(map(int, input("enter the values:").split(",")))
print(a+b)'''

'''a,b = tuple(map(int, input("enter the values:").split(",")))
print(a)'''

'''a,b = set(map(int, input("enter the values:").split(",")))
print(a)'''

a = input("enter key value pairs")
b = dict(i.split(":") for i in a.split(","))
print(b)
