Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#logical
a=7
b=14
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a>b or b>a
True
a!=b or a==b
True
not True
False
not False
True
#identify
a=7
type(a) is int
True
type(a) is not int
False
a="prashanthi"
type(a) is str
True
type(a) is not str
False
a=7+7j
type(a) is complex
True
type(a)is not complex
False
a=7.7
type(a)is float
True
type(a)is not float
False
a=7,6,5,4,3,2,1
9 in a
False
7 in a
True
9 not in a
True
7 not in a
False

#bitwise
a=3
>>> b=6
>>> a&b
2
>>> a=4
>>> b=8
>>> a|b
12
>>> a=7
>>> ~a
-8
>>> a=-7
>>> ~a
6
>>> -(a+1)
6
>>> -(a+1)
6
>>> a=7
>>> b=14
>>> a^b
9
>>> a=5
>>> b=10
>>> a^b
15
>>> a=7
>>> a<<2
28
>>> a=2
>>> a>>3
0
>>> a=7
>>> a<<2
28
>>> a=8
>>> a>>2
2
