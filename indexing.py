Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 'vijayawada'
a[0]
'v'
a[1]
'i'
a[5]
'a'
a[10]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[10]
IndexError: string index out of range
a[9]
'a'
a[-1]
'a'
a[-10]
'v'
b = 'i am in class'
b[0]
'i'
b[1]
' '
b[8]
'c'
>>> b[9]
'l'
>>> b[-6]
' '
>>> b[-4]
'l'
>>> c = 'i love python'
>>> c[2] + c[3] + c[4] + c[5]
'love'
>>> c[7] + c[8] + c[9] + c[10] + c[11] + c[12]
'python'
>>> d = 'time is very precious'
>>> d[13] + d[14] + d[15] + d[16] + d[17] + d[18] + d[19] +  d[20]
'precious'
>>> d[8] + d[9] +  d[10] + d[11]
'very'
>>> d[0] + d[1] +  d[2] + d[3]
'time'
>>> e = 'work hard'
>>> e[-6] + e[-7] + e[-8] + e[-9]
'krow'
>>> e[-9] + e[-8] + e[-7] e[-6]
SyntaxError: invalid syntax
>>> e[-9] + e[-8] + e[-7] + e[-6]
'work'
>>> e[-4] + e[-3] + e[-2] + e[-1]
'hard'
>>> f = 'i am learning python'
>>> f[-15] + f[-14] + f[-13] + f[-12] + f[-11]
'learn'
>>> f[-18] + f[-17]
'am'
>>> f[-6] + f[-5] + f[-4] + f[-3] + f[-2] + f[-1]
'python'
