Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strip
#lstrip,rstrip
a="prashanthi"
a.strip()
'prashanthi'
a="   prashanthi    "
a.strip()
'prashanthi'
a.rstrip()
'   prashanthi'
a.lstrip()
'prashanthi    '
a.strip()
'prashanthi'
#split()
a"python,java,sql,c++"
SyntaxError: invalid syntax
a="pyhton,java,sql,c++"
a.split()
['pyhton,java,sql,c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']
c=b.split()
c
['i', 'am', 'learning', 'python']
c[4].lower()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c[4].lower()
IndexError: list index out of range
c[4].upper()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c[4].upper()
IndexError: list index out of range
b[4].upper()
' '
b[1].upper()
' '
d="data analysis"
d[1].upper()
'A'
e="i am lerning python full stack"
e.split(e)
['', '']
e=split()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    e=split()
NameError: name 'split' is not defined
e.split()
['i', 'am', 'lerning', 'python', 'full', 'stack']
e[1].upper()
' '
#join
a="apple,banana,grapes"
"".join(a)
'apple,banana,grapes'
" ".join(a)
'a p p l e , b a n a n a , g r a p e s'
"p".join()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    "p".join()
TypeError: str.join() takes exactly one argument (0 given)
"p".join(a)
'appppplpep,pbpapnpapnpap,pgprpapppeps'
p="hello"
"k".join(p)
'hkeklklko'
#concatenation()
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="prashanthi"
lname="kokkiligadda"
print(fname+lname)
prashanthikokkiligadda
print(fname+" "+lname)
prashanthi kokkiligadda
print(fname.title()+lname.title())
PrashanthiKokkiligadda
print(fname.title()+" "+lname.title())
Prashanthi Kokkiligadda
print(fname+" "+lname).title())
SyntaxError: unmatched ')'
print((fname+" "+lname).title())
Prashanthi Kokkiligadda
#join
a"mango apple bread"
SyntaxError: invalid syntax
a="mango apple"
" ".join(a)
'm a n g o   a p p l e'
"".join(a)
'mango apple'
"p".join(a)
'mpapnpgpop pappppplpe'
#formatting
a=7
b=10
print(a+b)
17
>>> print("the sum is",a+b)
the sum is 17
>>> city="vijayawada"
>>> print("city is ",city)
city is  vijayawada
>>> name="prashanthi kokkiligadda"
>>> print("her name is",name)
her name is prashanthi kokkiligadda
>>> #format
>>> a="motu"
>>> b="patlu"
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> #fstring
>>> a="sweety"
>>> b="cuty"
>>> print(f"hello {a}{b}")
hello sweetycuty
>>> print(f"hello {a} {b}")
hello sweety cuty
>>> print(f"hello {a} hello{b}")
hello sweety hellocuty
>>> print(f"hello {a} hello {b}")
hello sweety hello cuty
>>> #fomatting format fstring
>>> a=6
>>> b=10
>>> print("the multiply of 6&10".format(a,b))
the multiply of 6&10
>>> print(a+b)
16
>>> print("the multiply of 6&10",a+b)
the multiply of 6&10 16
print(a*b)
60
print("the multiply of 6&10",a*b)
the multiply of 6&10 60
