Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> a=10
>>> b=10.5
>>> c="hiii"
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
>>> d=str(a)
>>> d
'10'
>>> type(d)
<class 'str'>
>>> l=[10,"welcome",2.5]
>>> l[1]
'welcome'
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> l
[10, 'welcome', 2.5]
>>> l.append()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l.append()
TypeError: append() takes exactly one argument (0 given)
>>> l.append("")
>>> l
[10, 'welcome', 2.5, '']
>>> l.append("rvr")
>>> l
[10, 'welcome', 2.5, '', 'rvr']
>>> l1=12,15
>>> l.append(l1)
>>> l
[10, 'welcome', 2.5, '', 'rvr', (12, 15)]
>>> l.append(["hello","it"])
>>> l
[10, 'welcome', 2.5, '', 'rvr', (12, 15), ['hello', 'it']]
>>> l[6]
['hello', 'it']
>>> l.extend(["hello","it"])
>>> l
[10, 'welcome', 2.5, '', 'rvr', (12, 15), ['hello', 'it'], 'hello', 'it']
>>> l[7]
'hello'
>>> l2=[2,2,"a","b","c","b"]
>>> l2.count("b")
2
>>> l2.sort()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l2.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l3=["b","a","h","c"]
>>> l3.sort()
>>> l3
['a', 'b', 'c', 'h']
>>> l3.pop()
'h'
>>> l3
['a', 'b', 'c']
>>> l3.pop(1)
'b'
>>> l3
['a', 'c']
>>> l2
[2, 2, 'a', 'b', 'c', 'b']
>>> l2.insert(1,"IT")
>>> l2
[2, 'IT', 2, 'a', 'b', 'c', 'b']
>>> l[2]="two"
>>> l2[2]="two"
>>> l2
[2, 'IT', 'two', 'a', 'b', 'c', 'b']
>>> l2.index("IT")
1
>>> l2.reverse()
>>> l2
['b', 'c', 'b', 'a', 'two', 'IT', 2]
>>> l2.remove()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    l2.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> l2.remove(1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    l2.remove(1)
ValueError: list.remove(x): x not in list
>>> l2.remove("a")
>>> l2
['b', 'c', 'b', 'two', 'IT', 2]
>>> del l2
>>> l2
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    l2
NameError: name 'l2' is not defined
>>> l1
(12, 15)
>>> l
[10, 'welcome', 'two', '', 'rvr', (12, 15), ['hello', 'it'], 'hello', 'it']
>>> l.clear()
>>> l
[]
>>> l=[1,2,3]
>>> l1=l.copy()
>>> l1
[1, 2, 3]
>>> l
[1, 2, 3]
>>> l3=l2
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    l3=l2
NameError: name 'l2' is not defined
>>> l3=l1
>>> l3
[1, 2, 3]
>>> l.append("hh")
>>> l
[1, 2, 3, 'hh']
>>> l1
[1, 2, 3]
>>> l3
[1, 2, 3]
>>> l2.append("hello")
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    l2.append("hello")
NameError: name 'l2' is not defined
>>> l1.append("hello")
>>> l1
[1, 2, 3, 'hello']
>>> l3
[1, 2, 3, 'hello']
>>> 
