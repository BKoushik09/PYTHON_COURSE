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

'''a generator is also a function which can be used as an iterator(loop) by producing group of values,
where we use yield keyword.'''

#yield vs return
#return will terminate the function whereas yield can pass the function and go on with every successive iteration
'''a, b = [int(x) for x in input("enter the values:").split(",")]
def check(a,b):
    while a<b:
        yield a
        a = a+1
        yield a
print(*check(a,b))'''

'''a, b = [int(x) for x in input("enter the values:").split(",")]
def check(a,b):
    while a<b:
        a = a+1
        return a
    #return a
print(check(a,b))'''

#yield vs return example
'''def hello():
    return "python"
    return "java"
    return "sql"
    #return "python","java","sql"
print(hello()) #it prints only python, because return will terminate the function'''

'''def hello():
    yield "vijayawada"
    yield "hyderabad"
    yield "vizag"
print(*hello()) # * is used to unpack the values'''

#next() function---> prints only one value in one line
'''def hello():
    yield "vijayawada"
    yield "hyderabad"
    yield "vizag"
d = hello()
print(next(d))
print(next(d))
print(next(d))
print(next(d))  #this print() raises error: StopIteration'''
