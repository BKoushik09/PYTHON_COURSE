Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dict()
a = {"name" : "koushik", "year" : 2004, "month" : 2}
print(a)
{'name': 'koushik', 'year': 2004, 'month': 2}
type(a)
<class 'dict'>
b = {'name', 'year', 'month'}
print(b)
{'month', 'year', 'name'}
type(b)
<class 'set'>
#keys()
a.keys()
dict_keys(['name', 'year', 'month'])
#values()
a.values()
dict_values(['koushik', 2004, 2])
#items()
a.items()
dict_items([('name', 'koushik'), ('year', 2004), ('month', 2)])
#accessing
a["name"]
'koushik'
a['year']
2004
a['month']
2
#update()
print(a)
{'name': 'koushik', 'year': 2004, 'month': 2}
a.update({"mail id" : "koushik@gmail.com"})
a
{'name': 'koushik', 'year': 2004, 'month': 2, 'mail id': 'koushik@gmail.com'}
a
{'name': 'koushik', 'year': 2004, 'month': 2, 'mail id': 'koushik@gmail.com'}
a.update({'city':'vijayawada', 'pincode':520015})
>>> a
{'name': 'koushik', 'year': 2004, 'month': 2, 'mail id': 'koushik@gmail.com', 'city': 'vijayawada', 'pincode': 520015}
>>> #set_default()
>>> a = {"hours" : 6, 'minutes' : 15, 'seconds' : 6}
>>> a.set_default('date',20)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.set_default('date',20)
AttributeError: 'dict' object has no attribute 'set_default'. Did you mean: 'setdefault'?
>>> a.setdefault('date',20)
20
>>> a
{'hours': 6, 'minutes': 15, 'seconds': 6, 'date': 20}
>>> #pop()
>>> a
{'hours': 6, 'minutes': 15, 'seconds': 6, 'date': 20}
>>> a.pop(1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.pop(1)
KeyError: 1
>>> a.pop('hours')
6
>>> a
{'minutes': 15, 'seconds': 6, 'date': 20}
>>> #popitem()
>>> a.popitem()
('date', 20)
>>> a
{'minutes': 15, 'seconds': 6}
