Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#SETS AND IT'S METHODS
a = {3, 5.6, 'koushik', 5+9j, True, False}
print(a)
{False, True, (5+9j), 3, 5.6, 'koushik'}
type(a)
<class 'set'>
b = {5, 6, 7, 8, 9}
print(b)
{5, 6, 7, 8, 9}
type(b)
<class 'set'>
#issubset()
a = {2, 3, 4, 5, 6, 7}
b = {5, 6, 7}
b.issubset(a)
True
a.issubset(b)
False
#add()
a = {1.1, 2.2, 3.3, 4.4, 5.5}
a.add(6.6)
a
{1.1, 2.2, 3.3, 4.4, 5.5, 6.6}
#issuperset()
a = {3, 4, 5, 6, 7, 8, 9}
b = {2, 3, 4,5, 6}
a.issuperset(b)
False

a = {0, 1, 2, 3, 4, 5}
b = {0, 3, 5}
a.issuperset(b)
True
b.issubset(a)
True
#union()
a = {10, 20, 30, 40, 50}
b = {40, 50, 60, 70, 80}
a.union(b)
{70, 40, 10, 80, 50, 20, 60, 30}
#intersection()
a = {11, 22, 33, 44, 55, 66, 77}
b = {11, 44, 99, 88}
a.intersection(b)
{11, 44}
#difference()
a.difference(b)
{33, 66, 77, 22, 55}
b.difference(a)
{88, 99}
#update()
a = {1, 11, 111, 1111, 11111}\
b = {2, 22, 222, 2222, 22222}
SyntaxError: invalid syntax
a
{33, 66, 22, 55, 11, 44, 77}
a = {1, 11, 111, 1111, 11111}
b = {2, 22, 222, 2222, 22222}
a.update(b)
b
{2, 222, 22, 22222, 2222}
a
{1, 2, 11111, 11, 22222, 111, 2222, 22, 1111, 222}
b.update(a)
a
{1, 2, 11111, 11, 22222, 111, 2222, 22, 1111, 222}
b
{1, 2, 11111, 11, 22222, 2222, 111, 22, 1111, 222}
#difference_update()
a = {4, 5, 6, 7, 8, 9}
b = {2, 3, 4, 5, 6,7, 8, 9, 10}
a.difference_update(b)
a
set()
a = {2, 3, 4, 5 ,6, 7}
b = {1, 5, 7, 9, 11, 12}
a.difference_update(b)
a
{2, 3, 4, 6}
a
{2, 3, 4, 6}
b.difference_update(a)
b
{1, 5, 7, 9, 11, 12}
#symmetric_difference()
a = {3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 8, 9, 10, 11}
a.symmetric_difference(b)
{1, 2, 4, 5, 6, 7, 10, 11}
a
{3, 4, 5, 6, 7, 8, 9}
b.symmetric_difference(a)
{1, 2, 4, 5, 6, 7, 10, 11}
b
{1, 2, 3, 8, 9, 10, 11}
#symmetric_difference_update()
a = {1, 3, 5, 7, 9, 11, 13}
b = {2, 3, 4, 6, 8, 10, 12}
a.symmetric_difference_update(b)
a
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
a
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b
{2, 3, 4, 6, 8, 10, 12}
b.symmetric_difference_update(a)
b
{1, 3, 5, 7, 9, 11, 13}
#intersection_update()
a = {7, 8, 9, 10, 11, 12}
b = {4, 5, 6, 7, 8, 9}
a.intersection_update(b)
a
{8, 9, 7}
b.intersection_update(a)
b
{8, 9, 7}
a
{8, 9, 7}
#pop()
a = {1, 3, 5, 7, 9}
a.pop()
1
a.pop(4)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
#remove()
a.remove(7)
a
{3, 5, 9}
#copy()
a = {99, 88, 77,66}
a.copy()
{88, 66, 99, 77}
#clear()
a.clear()

a
set()
#discard()
a.discard(2)
>>> a
set()
>>> #isdisjoint()
>>> a = {3, 4, 5}
>>> b = {6, 7, 8}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(a)
True
>>> a = {1, 2, 3, 4, 5}
>>> b = {5, 6, 7, 8, 9}
>>> a.isdisjoint(b)
False
>>> b.isdisjoint(a)
False
>>> #len()
>>> len(a)
5
>>> #count()
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> #index()
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
