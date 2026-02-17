Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#VARIABLES
print(09+11)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
print(9+11)
20
a = 11
print(a)
11
b = 9
print9b)
SyntaxError: unmatched ')'
print(b)
9
k = 100000
print(k)
100000
a1234566789 = 123456789
print(a123456789)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(a123456789)
NameError: name 'a123456789' is not defined. Did you mean: 'a1234566789'?
print(a1234566789)
123456789
city = 'vijayawada'
print(city)
vijayawada
name = 'koushik'
print(name)
koushik
color = 'blue'
print(color)
blue
first name = "koushik"
SyntaxError: invalid syntax
first_name = "koushik"
print(first_name)
koushik
@a = 100
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
_a = 20
print(_a)
20
email = "koushik@gmail.com"
print(email)
koushik@gmail.com
a, b = 3, 4
print(a+b)
7
a = 3
b = 4
print(a+b)
7
a = 3, b = 4
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a = 6; b = 8
print(a+b)
14
fname, lname = 'koushik', 'b'
print(fname + lname)
koushikb
>>> print(fname + ' ' + lname)
koushik b
>>> fname = 'koushik'; lname = 'B'
>>> print(fname+lname)
koushikB
>>> x = 6
>>> print(x)
6
>>> del x
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> #case sensitive
>>> country = 'India'
>>> print(country)
India
>>> print(Country)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(Country)
NameError: name 'Country' is not defined. Did you mean: 'country'?
>>> age = 21
>>> print(age)
21
>>> print(AGE)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(AGE)
NameError: name 'AGE' is not defined
>>> AGE = 20
>>> print(AGE)
20
