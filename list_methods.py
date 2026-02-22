Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a, b = 9, 11
print(f"the result is: {a*b}")
the result is: 99
print("the result is {}".format(a*b))
the result is 99
#LIST METHODS
a = [0, 11.9, 'python', 9+11j, True, False]
a
[0, 11.9, 'python', (9+11j), True, False]
type(a)
<class 'list'>
#append()
a.append("AI")
a
[0, 11.9, 'python', (9+11j), True, False, 'AI']
a.append(000)
a
[0, 11.9, 'python', (9+11j), True, False, 'AI', 0]
a.append("ML", "DL")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ML", "DL")
TypeError: list.append() takes exactly one argument (2 given)
#extend()
a.extend("html", "css")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.extend("html", "css")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["html", "css"])
a
[0, 11.9, 'python', (9+11j), True, False, 'AI', 0, 'html', 'css']
#insert()
b = ['apple', 'mango', 'banana']
b.insert(1, 'kiwi')
b
['apple', 'kiwi', 'mango', 'banana']
b.insert('berry', 2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.insert('berry', 2)
TypeError: 'str' object cannot be interpreted as an integer
c = ['black', 'white', 'red', 'blue']
#index()
c.index('white')
1
c.index('green')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c.index('green')
ValueError: 'green' is not in list
c.index("red")
2
#copy()
b = a.copy()
b
[0, 11.9, 'python', (9+11j), True, False, 'AI', 0, 'html', 'css']
c = a.copy()
c
[0, 11.9, 'python', (9+11j), True, False, 'AI', 0, 'html', 'css']
b = c.copy()
b
[0, 11.9, 'python', (9+11j), True, False, 'AI', 0, 'html', 'css']
#sort()
d = ['biryani', 'icecream', 'chocolates']
d.sort()
d
['biryani', 'chocolates', 'icecream']
d = [3, 5, 2, 9, 1, 2, 6, 8, 7]
d.sort()
d
[1, 2, 2, 3, 5, 6, 7, 8, 9]
d = [-8, -10, -3, -5, 11, 9, 10, 0, -1, -5]
d.sort()
d
[-10, -8, -5, -5, -3, -1, 0, 9, 10, 11]
#reverse()
a = ['ml', 'ds', 'ai', 'dl']
a.reverse()
a
['dl', 'ai', 'ds', 'ml']
#pop()
a = ['html', 'css', 'js']
a.pop()  #if we didn't specify any index number, it will delete last element
'js'
a
['html', 'css']
a.pop('css')  #we must specify index number not element name
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.pop('css')  #we must specify index number not element name
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'css'
a
['html']
a.pop(0)
'html'
a
[]
#remove()
a = ['hi', 'hello', 'namaste']
a.remove('hi')
a
['hello', 'namaste']
#len()
a = 'code'
len(a)
4
b = ['code']
len(b)
1
#count()
a = ['sun', 'star', 'sky', 'moon']
a.count('sky')
1
>>> #clear()
>>> a = ['earth', 'mars', 'jupyter', 'saturn', 'pluto']
>>> a.clear()
>>> a
[]
>>> a.append('mercury')
>>> a
['mercury']
>>> a = [9, 1, 5, 2, 8, 4, 6, 3, 7, 0]  #op:[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> b = [9, 1, 5, 2, 8]
>>> b.sort()
>>> b
[1, 2, 5, 8, 9]
>>> b.reverse()
>>> b
[9, 8, 5, 2, 1]
>>> c = [4, 6, 3, 7, 0]
>>> c.sort()
>>> c
[0, 3, 4, 6, 7]
>>> c.reverse()
>>> c
[7, 6, 4, 3, 0]
>>> c.append(b)
>>> print(c.append(b))
None
>>> print(c+b)
[7, 6, 4, 3, 0, [9, 8, 5, 2, 1], [9, 8, 5, 2, 1], 9, 8, 5, 2, 1]
>>> c
[7, 6, 4, 3, 0, [9, 8, 5, 2, 1], [9, 8, 5, 2, 1]]
