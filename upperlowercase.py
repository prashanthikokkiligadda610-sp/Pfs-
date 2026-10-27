Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#upper()
a="code"
a.upper()
'CODE'
b="prashanthi"
b.upper()
'PRASHANTHI'
c="HELLO"
c.lower()
'hello'
d="PRASHANTHI"
d.lower()
'prashanthi'
a="python"
a[0].upper()
'P'
a[1].upper()
'Y'
a="i am from vijayawada"
a.capitalize()
'I am from vijayawada'
b="python full stack trainee"
a.title()
'I Am From Vijayawada'
b.title()
'Python Full Stack Trainee'
c="kokkiligadda prashanthi"
c.lower()
'kokkiligadda prashanthi'
c.upper()
'KOKKILIGADDA PRASHANTHI'
c.title()
'Kokkiligadda Prashanthi'
c.capitalize()
'Kokkiligadda prashanthi'
b="python COURSE"
b.upper()
'PYTHON COURSE'
a="softskills"
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isdigital()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.isdigital()
AttributeError: 'str' object has no attribute 'isdigital'. Did you mean: 'isdigit'?
b="codegnan at vijayawada"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b.alpha()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
b.isdigital()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b.isdigital()
AttributeError: 'str' object has no attribute 'isdigital'. Did you mean: 'isdigit'?
a=1234
a.isdigital()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.isdigital()
AttributeError: 'int' object has no attribute 'isdigital'
a="1234"
a.isdigital
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.isdigital
AttributeError: 'str' object has no attribute 'isdigital'. Did you mean: 'isdigit'?
a.isdigital()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.isdigital()
AttributeError: 'str' object has no attribute 'isdigital'. Did you mean: 'isdigit'?
>>> a.isdigit()
True
>>> p="61072986"
>>> p.isdigit()
True
>>> k="prashanthi"
>>> a.startswith(p)
False
>>> a.startswith(r)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.startswith(r)
NameError: name 'r' is not defined
>>> a.endswith(i)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.endswith(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> k.startswith(p)
False
>>> k.endswith(i)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    k.endswith(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> k.endswith("i")
True
>>> c="ksp@123"
>>> c.isalnum()
False
>>> k.startswith("p)
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> k.startswith("p")
...              
True
