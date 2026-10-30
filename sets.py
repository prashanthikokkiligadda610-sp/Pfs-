Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={7,7.6,"prashanthi",7+7j,True,False}
print(a)
{False, True, 7.6, 7, 'prashanthi', (7+7j)}
type(a)
<class 'set'>
b={7,4,4,3,7,2,9,8,10}
print(b)
{2, 3, 4, 7, 8, 9, 10}
#add
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
#subset
a={7,8,9,3,4,5}
b={7,8,9,,2,1,6}
SyntaxError: invalid syntax
a={7,8,9,3,4,5}
b={7,8,9,2,1,6}
b.issubset(a)
False
a.issubset(a)
True
a={4,5,6}
b={1,2,3}
a.issubset(b)
False
#superset
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={5,6,7,8,9,10}
b={6,7,8,9,10,11,12}
a.union(b)
{5, 6, 7, 8, 9, 10, 11, 12}
b.union(a)
{5, 6, 7, 8, 9, 10, 11, 12}
#intersection
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
b.intersection(b)
{7, 8, 9, 10, 11, 12}
a.intersection(b)
{8, 9, 7}
b.intersection(a)
{8, 9, 7}
#update
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
b.update(b)

b
{7, 8, 9, 10, 11, 12}
a.update(b)
a
{4, 5, 6, 7, 8, 9, 10, 11, 12}
b.update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11, 12}
a={3,4,5,6,7,8}
b={8,9,10,11,12}
a.difference(b)
{3, 4, 5, 6, 7}
b.difference(a)
{9, 10, 11, 12}
a={1,2,3}
b={3,4,5}
a.difference(b)
{1, 2}
a={1,2}
b={3,4}
a.difference(b)
{1, 2}
#symmetric difference
a={10,11,12,13,14,15}
b={13,14,15,16,17,18}
a.symmetric_difference(b)
{10, 11, 12, 16, 17, 18}
b.symmetric_difference(a)
{10, 11, 12, 16, 17, 18}
a={1,2,3}
b={4,5,6}
a.symmetric_difference(b)
{1, 2, 3, 4, 5, 6}
#intersection update
a={8,9,10,11,12}
b={11,12,13,14,15}
a.intersection_update(b)
a
{11, 12}
b.intersection_update(a)
b
{11, 12}
a={1,2,3}
b={4,5,6}
a.intersection_update(b)
a
set()
b.intersection_update(a)
b
set()
#differenceupdate
a={10,20,30,40,50}
b={30,40,50,60,70}
a.difference_update(b)
a
{20, 10}
b.difference_update(a)
b
{50, 70, 40, 60, 30}
a={1,2,3}
b={4,5,6}
a.difference_update(a)
a
set()
a.difference_update(b)
a
set()
#symmetricdifferenceupdate
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}
#pop
a={7,8,9,10,11,12}
a.pop()
7
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a
{8, 9, 10, 11, 12}
a.remove(12)
a
{8, 9, 10, 11}
a.discard(9)
a
{8, 10, 11}
a.pop()
8
a
{10, 11}
a.remove(10)
a
{11}
a.discard(11)
a
set()
#copy
a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
b=a.copy()
b
{50, 20, 40, 10, 30}
#clear
a={100,200,300,400}
a.clear()
a
set()
#add
>>> a={10,100,1000,10000}
>>> a.clear()
>>> a
set()
>>> a.add(1000000)
>>> a
{1000000}
>>> #index
>>> a{5,6,7,8,9,10}
SyntaxError: invalid syntax
>>> a={5,6,7,8,9}
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
>>> len(a)
5
>>> a.count(10)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    a.count(10)
AttributeError: 'set' object has no attribute 'count'
>>> a.count(9)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    a.count(9)
AttributeError: 'set' object has no attribute 'count'
>>> #isdisjoint
>>> a={4,5,6,7,8}
>>> b={9,10,11,12}
>>> a.isdisjoint(b)
True
>>> a={3,4,5,6,7}
>>> b={7,8,9,10}
>>> a.isdisjoint(b)
False
