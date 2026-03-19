#FUNCTIONS
'''1. a function is a block of organized, reusable code that is used to perform a single or multiple tasks
2. python use in built functions like print, you can make your own function also.
    and these are called user defined functions
3. function blocks begin with the keyword def followed by the function name and paranthesis ()'''

'''def calculate(a, b):
    print("the sum is:", a+b)
    print("the difference is:", a-b)
    print("the product is:", a*b)
    print("the power of a is:", a**b)
    print("the remainder is:", a%b)
    print("the integer division is:", a//b)
calculate(10, 20)
calculate(73, 87)'''

#runtime
'''def add():
    a = int(input("enter a value:"))
    b = int(input("enter b value:"))
    print(a+b)
add()'''

'''def fullname():
    fname = input("enter first name:")
    lname = input("enter last name:")
    print((fname + " " + lname.title()))
fullname()'''

#print vs return
#print just shows the user output to console
#return is used to terminate the function and gives back a value from the function
'''def cal(a, b):
    c = a+b
    d = a-b
    e = a*b
    #return c
    #return d
    #return e
    return c, d, e
print(cal(9, 11))'''

#EXAMPLE-1 (method-1)
'''def hello():
    a = int(input("enter a value:"))
    b = int(input("enter b value:"))
    print("for addition choose option 1\nfor subtraction choose option 2\nfor multiplication choose option 3")
    option = int(input("choose option 1/2/3:"))
    if option==1:
        print("addition is:", a+b)
    elif option==2:
        print("subtraction is:", a-b)
    elif option==3:
        print("multiplication is:", a*b)
    else:
        print("choose correct option")
hello()'''

#EXAMPLE-1 (method-2)
'''def add():
    print("addition is:", a+b)
def sub():
    print("subtraction is:", a-b)
def mul():
    print("multiplication is:", a*b)
while True:
    a = int(input("enter a value:"))
    b = int(input("enter b value:"))
    print("for addition choose option 1\nfor subtraction choose option 2\nfor multiplication choose option 3")
    option = int(input("choose option 1/2/3:"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()
    else:
        print("choose correct option")'''

#EXAMPLE-2
'''def splitbill():
    a = int(input("enter the total persons:"))
    b = int(input("enter the total bill:"))
    print(b//a)
splitbill()'''

'''def splitbill():
    a = int(input("enter the total persons:"))
    b = int(input("enter the total bill:"))
    c = b//a
    print("bill per person is {}".format(c))
    print(f"the bill per person is {c}")
splitbill()'''

#---------------------FUNCTIONS WITH ARGUMENTS---------------------------
#1.Keyword and Positional Arguments
'''def details(id, name, mailid):
    id = 10
    name = 'koushik'
    mailid = 'k@gmail.com'
    print(id, name, mailid)
details(id = 'id', name = 'name', mailid = 'mailid')''' #METHOD-1

'''def details(id, name, mailid):
    print(id, name, mailid)
details(id = 'id', name = 'name', mailid = 'mailid')
details(id = '10', name = 'gopi', mailid = 'g@gmail.com') #method-2
details(id = '20', name = 'neeraja', mailid = 'n@gmail.com')
details(40, 'koushik', 'k@gmail.com') #method-3
details('koushik', 'k@gmail.com', 40) #it will print in this order
details(mailid = 'n@gmail.com', id = 50, name = 'niharika') #method-4'''

#2.Default Arguments
'''def grocery(item, price):
    print("Item is %s" %item)
    print("price is %d" %price)
grocery('sugar', 50)'''  #method-1

'''def grocery(item = 'sugar', price = 50):
    print("Item is %s" %item)
    print("price is %d" %price)
grocery()'''  #method-2

'''def grocery(item, price = 50):
    print("item is %s" %item)
    print("price is %d" %price)
grocery('sugar')'''  #method-3

'''def grocery(item = 'sugar', price):  #raises error
    print("Item is %s" %item)
    print("price is %d" %price)
grocery(50)'''  #method-4

#example
'''def cake(name, price, quantity):
    print("cake name is %s" %name)
    print("cake price is %d" %price)
    print("cake quantity is %.2f" %quantity)
cake('butter scotch', 100, 30)'''

'''def cake(name = 'butter scotch', price = 100, quantity = 30):
    print("cake name is %s" %name)
    print("cake price is %d" %price)
    print("cake quantity is %.2f grams" %quantity)
cake()'''

#3. * arguments --> * used to unpack the elements
'''a = [2, 3, 4, 5,6, 7, 8, 9]
print(a)
print(*a)

b = (2, 3, 4, 5, 6, 7, 8, 9)
print(b)
print(*b)

c = {2, 3, 4, 5, 6, 7, 8, 9}
print(c)
print(*c)

d = {'month': 10, "year": 2026}
print(d)
print(*d)'''

'''a, b, c = 1, 2, 3, 4, 5, 6, 7, 8, 9 
print(a)
print(b)
print(c)''' #raises error

'''a, *b, c = 1, 2, 3, 4, 5, 6, 7, 8, 9 
print(a)
print(*b)
print(c)'''

'''*a, b, c = 1, 2, 3, 4, 5, 6, 7, 8, 9 
print(*a)
print(b)
print(c)'''

'''a, *b, *c = 1, 2, 3, 4, 5, 6, 7, 8, 9  #error: multiple star assignments occured
print(a)
print(*b)
print(*c)'''
 
'''a = 'koushik'
print(a)
print(*a)'''

#4.variable length arguments
#variable length arguments are automatically stores in tuple and we use * argument
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2, 3, 4, 5, 6, 7)
d = [5, 6, 7, 8, 9, 10]
check(d)
e = (3, 4, 5, 6, 7)
check(*e)
f = {"name":"koushik", "city":"vijayawada"}
check(*f)'''

'''def check1(*a):
    d = 2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int, float):
        #if type(i)==int or type(i)==float:
            d = d+i
            print(d)
check1()
check1(2, 3, 4, 5, 6)
check1(2, 3, 4, 3, 5, 6.2, 4.3)
check1(1, 3, 5, 6.2, 3.2, "pooja")'''

#kwargs(**a)
def details(**a):
    print(a)
    print(type(a))
details()
d = {"idnos":[10, 20, 30],
     "names":['koushik', 'gopi', 'neeraja'],
     "status":['p', 'a', 'p']
     }
details(**d)

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i, a[i])
    for i in a.items():
        print(i)
details()
d = {"idnos":[10, 20, 30],
     "names":['koushik', 'gopi', 'neeraja'],
     "status":['p', 'a', 'p']
     }
details(**d)'''

#both * and **
'''def final(*a, **b):
    d = 3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d = d+i
        print(d)
    for i,j in b.items():
        print("key is:", i)
        print("value is:", j)
final()
data = (2, 3, 4, 5, 2.3, 4.5)
final(*data)
details = {"names":['ssmb', 'pspk', 'chiru'],
           'marks':[100, 90, 80]
           }
final(**details)
final(*data, **details)'''

#Built-ins
'''print(max(4, 6, 8, 9, 11))
print(min(4, 6, 8, 9, 11))
a = 4, 6, 8, 9, 11
print(sum(a))
print(sum([4, 6, 8, 9, 11]))'''

n = int(input("enter number of students:"))
lst = []
present = 0; absent = 0
print("choose present or absent")
for i in range(n):
    a = input(f"student {i} status is:")
    lst.append(a)
if 'present' in lst:
    present+=1
else:
    absent+=1
print("total students are:", n)
print("total present are:", present)
print("total absent are:", absent)
    
    
