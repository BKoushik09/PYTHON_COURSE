#global and local variables
'''a variable inside and outside the function is called global and local variables
a variable defined above the function and accessible to the entire global space is called a global variable
a variable inside the function is called local variable'''

#global variable(example-1)
'''a = 3
def check():
    print("inside value is:", a)
check()
print("outside value is:", a)'''

#global variable(example-2)
'''a = 2
def check1():
    a = 5
    a = a**2
    print("inside value is:", a) #prints 25
check1()
print("outside value is:", a) #prints 2'''

#both global and local variables
'''a = 4
b = 3
def check2():
    a = 7
    print("inside value is:", a)
    a = 10
    print("updated value is:", a+5)
    b = 12 #local variable
    b = b+a
    print("value of b is:", b)
check2()
print("a value is:", a)
print("b value is:", b)'''

#Usage of global keyword
'''when user wants to access the global variable inside the function directly and
carry forward the updated value even outside the function, then we need to use global keyword'''

'''a = 5
def final():
    global a,b
    print("inside value is:", a)
    a = 10
    print("updated value is:", a)
    b = 15
    b = b+a
    print("value of b is:", b)
final()
print("a value is:", a)
print("b value is:", b)'''

#GENERATORS
'''no tuple comprehension in above cases if we remove those braces and keep paranthesis
then the outcome is generator'''
'''a = [i for i in range(20)]
print(a)
print(type(a))'''

'''a = (i for i in range(20))
print(a) #o/p:<generator object <genexpr> at 0x000001D6647462C0>
print(type(a)) #o/p:<class 'generator'>'''

'''a = (i for i in range(20))
print(*a)
print(type(a))'''

'''a = (i for i in range(20))
print(list(a))
print(tuple(a))
print(set(a))'''
