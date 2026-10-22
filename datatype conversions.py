Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int()
int(7)
7
int(7.8)
7
int("prashanthi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("prashanthi")
ValueError: invalid literal for int() with base 10: 'prashanthi'
int(True)
1
int(False)
0
#float
float(7)
7.0
float(7.5)
7.5
float("prashu")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float("prashu")
ValueError: could not convert string to float: 'prashu'
float(True)
1.0
float(False)
0.0
#string
str(7)
'7'
str(7.5)
'7.5'
str("prashanthi")
'prashanthi'
str(True)
'True'
str(False)
'False'
#complex()
complex(7)
(7+0j)
complex(7.5)
(7.5+0j)
complex(7+7j)
(7+7j)
complex(True)
(1+0j)
complex(False)
0j
#boolean
bool(7)
True
bool(7.5)
True
bool("Prashanthi")
True
bool("7+1j")
True
bool(True)
True
bool(False)
False
complex("prashanthi")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex("prashanthi")
ValueError: complex() arg is a malformed string
#arthemetic
a=6
b=10
print(a+b)
16
print(a-b)
-4
print(a*b)
60
print(a//b)
0
print(a/b)
0.6
print(a**b)
60466176
print(a%b)
6
a+b
16
a-b
-4
a*b
60
a//b
0
a/b
0.6
a**b
60466176
a%b
6
#assignment
2=8
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a=8
b=2
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
10
a-=b
b
2
a
8
a*=b
a
16
a//=b
a
8
a/=b
a
4.0
a**=b
a
16.0
a%=b
a
0.0
a=2
b=6
a+=b
b
6
a-=b
b
6
>>> a*=b
>>> b
6
>>> a//=b
>>> b
6
>>> a/=b
>>> b
6
>>> a**=b
>>> b
6
>>> a%=b
>>> b
6
>>> #comparision
>>> a=10
>>> b=20
>>> a<b
True
>>> a>
SyntaxError: invalid syntax
>>> a>b
False
>>> a<=b
True
>>> a>=b
False
>>> a!=b
True
>>> a==b
False
>>> a=10
>>> b=10
>>> a==b
True
