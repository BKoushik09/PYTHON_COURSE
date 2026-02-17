Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Data Types
a = 4
type(a)
<class 'int'>
b = 100
type(b)
<class 'int'>
c = 9.11
type(c)
<class 'float'>
d  = "code"
type(d)
<class 'str'>
e = "NRI"
type(e)
<class 'str'>
>>> f = '''python'''
>>> type(f)
<class 'str'>
>>> g = 'k'
>>> type(g)
<class 'str'>
>>> x = 5+9j
>>> type(x)
<class 'complex'>
>>> a = 5+9i
SyntaxError: invalid decimal literal
>>> y = 6j
>>> type(y)
<class 'complex'>
>>> b = j
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b = j
NameError: name 'j' is not defined
>>> p = True
>>> type(p)
<class 'bool'>
>>> q = False
>>> print(q)
False
>>> p = true
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    p = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> q = false
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    q = false
NameError: name 'false' is not defined. Did you mean: 'False'?
