Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#len()
a = 'bvsk koushik'
len(a)
12
b = 'data science'
len(b)
12
c = ''
len(c)
0
d = ' '
len(d)
1
#count()
a = 'johny johny yes papa'
a.count('johny')
2
a.count('a')
2
a.count(' ')
3
#find a string
x = 'string'
x.find('s')
0
x.find('i')
3
y = 'koushik'
y.find('k')
0
y.find('x')
-1
#escape sequences
#\n - new line
#\t - tab space
a = "name\nmobile number\nmail id\ncity"
a
'name\nmobile number\nmail id\ncity'
print(a)
name
mobile number
mail id
city
b = "name\tmobile number\tmail id\tcity"
print(b)
name	mobile number	mail id	city
#replace()
z = 'wait until you succeed'
z.replace('wait', 'work')
'work until you succeed'
p = 'wait until you succeed'
p = 'wait wait until you succeed'
p.replace('wait', 'work')
'work work until you succeed'
p = 'wait wait wait until you succeed'
p.replace('wait', 'work', 2)
'work work wait until you succeed'
#upper()
a = 'code'
a.upper()
'CODE'
#lower()
b = 'PYTHON FULL stack'
b.lower()
'python full stack'
#capitalize()
c = 'koushik'
c.capitalize()
'Koushik'
#title()
d = 'i am in vijayawada'
d.capitalize()
'I am in vijayawada'
d.title()
'I Am In Vijayawada'
d = 'anjani koushik boggavarapu'
d.title()
'Anjani Koushik Boggavarapu'
a = 'python'
a.isupper()
False
a.islower()
True
a.isalpha() #isalpha()
True
a = 'python full stack'
a.isalpha()
False
a.isdigit() #isdigit()
False
b = '12345'
b.isdigit()
True
#startswith()
a.startswith('p')
True
a.startswith('k')
False
#endswith()
a.endswith('k')
True
a.endswith('K')
False
#isalnum()
k = 'abc123'
k.isalnum()
True
z = 'abcd'
z.isalnum()
True
#strip(), lstrip(), rstrip()
a = '   koushik    '
a.strip()
'koushik'
a.lstrip()
'koushik    '
a.rstrip()
'   koushik'
#split()
a = 'python js react sql'
a.split()
['python', 'js', 'react', 'sql']
b = 'python is easy'
b.split()
['python', 'is', 'easy']
#join()
a = 'python', 'java', 'c++'
''.join(a)
'pythonjavac++'
' '.join(a)
'python java c++'
b = 'python' 'java' 'c++'
''.join(b)
'pythonjavac++'
#concatenation
a = 'good'
b = 'morning'
print(a + b)
goodmorning
print(a + ' ' + b)
good morning
print((a + ' ' + b).title())
Good Morning
a = 9
>>> b = 11
>>> #formatting
>>> print("the sum is:", a+b)
the sum is: 20
>>> a = 'koushik'
>>> b = 'boggavarapu'
>>> print('full name is:', (a+' '+b).title())
full name is: Koushik Boggavarapu
>>> #format()
>>> a = 'motu'
>>> b = 'patlu'
>>> print('hello {}{}', format(a,b))
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    print('hello {}{}', format(a,b))
ValueError: Invalid format specifier 'patlu' for object of type 'str'
>>> print('hello {}{}'.format(a,b))
hello motupatlu
>>> print('hello {} {}'.format(a,b))
hello motu patlu
>>> print('hello {} hi {}'.format(a,b))
hello motu hi patlu
>>> print('hello {} {}',format(a,b).title())
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print('hello {} {}',format(a,b).title())
ValueError: Invalid format specifier 'patlu' for object of type 'str'
>>> print('hello {} {}'.format(a,b).title())
Hello Motu Patlu
>>> a = 'john'
>>> b = 'cena'
>>> #fstring
>>> print(f"hello {a}{b}")
hello johncena
