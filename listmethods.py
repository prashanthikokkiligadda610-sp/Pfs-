Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 #list[]
a=[2,4.5,"prashanthi",7+7j,True,False]
print(a)
[2, 4.5, 'prashanthi', (7+7j), True, False]
type(a)
<class 'list'>
b=7.6
type(b)
<class 'float'>
c=[7.6]
type(c)
<class 'list'>
a=["python","c","java","c++"]
a.append("ai")
a
['python', 'c', 'java', 'c++', 'ai']
a.append("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ml","dsa")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","dsa"])
a
['python', 'c', 'java', 'c++', 'ai', ['ml', 'dsa']]
#extend
a=["dsa","ai","ml"]
a.extend(["python","java"])
a
['dsa', 'ai', 'ml', 'python', 'java']
#insert
b=["red","white"]
b.insert(1,"black")
b
['red', 'black', 'white']
['red', 'black', 'white']
['red', 'black', 'white']
#index
a=["apple","grapes","kiwi"]
a.index("mango")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.index("mango")
ValueError: list.index(x): x not in list
a.copy()
['apple', 'grapes', 'kiwi']
b=a.copy()
b
['apple', 'grapes', 'kiwi']
a.index("mango")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.index("mango")
ValueError: list.index(x): x not in list
ValueError: list.index(x): x not in list
SyntaxError: invalid syntax
#pop
a=["vij","vzg","hyd"]
a.pop()
'hyd'
a.pop(1)
'vzg'
a
['vij']
a.pop(0)
'vij'
a
[]
#remove
a=["hello","how","hii"]
a.remove("hii")
a
['hello', 'how']
a.remove("hello")
a
['how']
a.remove("how")
a
[]
#clear
a=["prashanthi","prashu","kprashanthi"]
a.clear()
a
[]
a.clear(0)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.clear(0)
TypeError: list.clear() takes no arguments (1 given)
b=[]
a.append("prashanthi")
a
['prashanthi']
#sort
a=
SyntaxError: invalid syntax
#sort
a=["kiwi","mango","apple","banana","grapes"]
a.sort()
a
['apple', 'banana', 'grapes', 'kiwi', 'mango']
p=[3,9,2,4,8,9,2]
p.sort()
p
[2, 2, 3, 4, 8, 9, 9]
d=[2,2.4,"python",4+5j]
d.sort()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
d=[True,False,True,False]
d.sort()
d
[False, False, True, True]
k=[2,3.4,4,21.4]
k.sort()
k
[2, 3.4, 4, 21.4]
#reverae
#reverse
a=["black","red","white"]
a.reverse()
>>> a
['white', 'red', 'black']
>>> b=[3,7,1,4,9,2]
>>> b.reverse()
>>> b
[2, 9, 4, 1, 7, 3]
>>> #count
>>> #length
>>> c=["python"]
>>> lebn(c)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    lebn(c)
NameError: name 'lebn' is not defined. Did you mean: 'len'?
>>> len(c)
1
>>> a=["java","ai","python"]
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> #count
>>> a.count("ai")
1
>>> a.count("0")
0
>>> a.count("java")
1
>>> b=["java","ai","a","ml"]
>>> b.count(a)
0
>>> a.count(a)
0
