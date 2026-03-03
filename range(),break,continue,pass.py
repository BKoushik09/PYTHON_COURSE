#range()
#start-stop-step
'''The range() returns a sequence of numbers, starting from 0 by default and
increments by one by one and stops before a specified number'''
'''for i in range(10):
    print(i)'''

'''for i in range(5,15):
    print(i)'''

'''for i in range(0,46,5):
    print(i, end=' ')
print()
for i in range(2,19,2):
    print(i, end=' ')
print()
for i in range(3,28,3):
    print(i, end=' ')'''

#EXAMPLE
'''while True:
    marks = int(input("enter the marks:"))
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(51,71):
        print("Grade D")
    else:
        print("Fail")'''

#break, continue and pass
'''
the break statement is used to terminate the entire loop
the continue statement is used to skips the current iteration and rest of the code will continue
the pass statement is a null statement. it does nothing but syntactically we need
'''

#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a = 10
while a>1:
    a = a-1
    if a==5:
        break
    print(a)'''

'''for i in range(20):
    if i==11:
        break
    print(i)'''

#continue
'''a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue'''

'''a=30
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)'''

'''a = 'python'
for i in a:
    if i=='t':
        continue
    print(i)'''

#pass
a=30
while a>20:
    print(a)
    a=a-1
    if a==25:
        pass
