#NESTED IF
'''a, b = 9, 11
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a, b = 9, 11
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a, b = 10, 20
if a==b:
    print("less")
    if b!=a:
        print("greater")
else:
    print("true")'''

'''a, b = 10, 20
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")
else:
    print("false")'''

''''a, b = 10, 20
if a<=b:
    print("less")
    if b==a:
        print("equal")
    elif a==b:
        print("not equal")
    else:
        print("true")'''

#EXAMPLE-1
'''while True:
    age = int(input("enter the age:"))
    if age<18:
        print("not eligible")
    else:
        print("eligible for vote")'''

#EXAMPLE-2
'''while True:
    number = int(input("enter any number:"))
    if number%2==0:
        print("even number")
    else:
        print("odd number")'''

#EXAMPLE-3
'''year = int(input("enter any year:"))
if year%4==0:
    print("leap year")
else:
    print("not leap year")'''

#EXAMPLE-4
'''vowels = 'AEIOUaeiou'
a = input("enter any alphabet:")
if a in vowels:
    print("it is vowel")
else:
    print("not vowel")'''

#EXAMPLE-5
'''name = 'Koushik'
a = input("enter any name:")
if a==name:
    print("welcome"+' ' + name)
else:
    print("welcome guest")'''

#EXAMPLE-6
'''names = ['koushik', 'gopi', 'neeraja', 'niharika', 'mahesh babu']
a = input("enter any name:").lower()
if a in names:
    print("welcome" + ' ' + a)
else:
    print("welcome guest")'''

#EXAMPLE-7
'''username = 'bvskak'
password = 1109
new_name = input("enter username:")
new_pass = int(input("enter your password"))
if new_name==username:
    if new_pass==password:
        print("Login successful")
    else:
        print("invalid password")
else:
    print("Invalid credentials")'''

#EXAMPLE-8
'''username = 'bvskak'
password = 1109
new_name = input("enter username:")
new_pass = int(input("enter your password"))
if new_name==username and new_pass==password:
    print("Login successful")
else:
    print("Invalid credentials")'''

#EXAMPLE-9
'''price = int(input("enter your price:"))
if price==1200:
    print("Red velvet cake")
elif price==1000:
    print("chocolate cake")
elif price==800:
    print("butterscotch cake")
elif price==600:
    print("choco almond cake")
else:
    print("Sorry!!!cake is not available")'''
