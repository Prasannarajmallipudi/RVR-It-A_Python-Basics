Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t = ()
>>> print(t)
()
>>> type(t)
<class 'tuple'>
>>> t = (172,"APSSDC",8989898989,'sdc@apssdc.in',"CSE")
>>> t
(172, 'APSSDC', 8989898989, 'sdc@apssdc.in', 'CSE')
>>> t[2]
8989898989
>>> t[-1]
'CSE'
>>> t[::-1]
('CSE', 'sdc@apssdc.in', 8989898989, 'APSSDC', 172)
>>> t
(172, 'APSSDC', 8989898989, 'sdc@apssdc.in', 'CSE')
>>> t=t[::-1]
>>> t
('CSE', 'sdc@apssdc.in', 8989898989, 'APSSDC', 172)
>>> dir(t)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t.count(172)
1
>>> t.count(2)
0
>>> t.count("CSE")
1
>>> t.index("CSE")
0
>>> t[1]="RVR"
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t[1]="RVR"
TypeError: 'tuple' object does not support item assignment
>>> del t
>>> t
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> 
