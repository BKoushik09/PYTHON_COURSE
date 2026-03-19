#Anonymous Functions(lambda function)
#anonymous functions are nameless functions we use a keyword called as lambda to create anonymous functions
'''def cal():
    x=5
    print(2*x+5)
cal()'''

#syntax: var=lambda arg:expr
'''a = lambda x:2*x+5
print(a(5))'''

'''a = int(input("enter a value:"))
b = lambda x:2*x+5
print(b(a))'''

'''a = int(input("enter a value:"))
b = int(input("enter b value:"))
c = lambda a,b:a*b
print(c(a,b))'''

'''a = lambda x,y:x*y
print(a(9,11))'''

'''a = input("enter any string:")
b = lambda x:x.upper()
print(b(a))'''

'''a = input("enter name:")
b = input("enter name:")
c = lambda x,y:a+b
print(c(a,b))'''

'''a,b = [x for x in input("enter the name:").split(",")]
c = lambda x,y:a+b
print(c(a,b))'''
