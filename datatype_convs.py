Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#datatype conversions
#int()
int(7)
7
int(7.8)
7
int("koushik")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("koushik")
ValueError: invalid literal for int() with base 10: 'koushik'
int(7+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(7+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float()
float(3)
3.0
float(9.11)
9.11
float("koushik")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("koushik")
ValueError: could not convert string to float: 'koushik'
float(1+2j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(1+2j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string()
str(1)
'1'
str(0.1)
'0.1'
str('hello')
'hello'
>>> str(9+11j)
'(9+11j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(1)
(1+0j)
>>> complex(1.1)
(1.1+0j)
>>> complex("koushik")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("koushik")
ValueError: complex() arg is a malformed string
>>> complex(1+2j)
(1+2j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(1)
True
>>> bool(1.1)
True
>>> bool("bye")
True
>>> bool(2+3j)
True
>>> bool(True)
True
>>> bool(False)
False
