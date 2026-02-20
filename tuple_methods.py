Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #TUPLE --> it is immutable
>>> a = (3, 3.6, 'hi', 5+9j, True, False)
>>> print(a)
(3, 3.6, 'hi', (5+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index("hi")
2
>>> a.count(False)
1
