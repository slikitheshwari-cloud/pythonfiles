Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5
id(a)
140721286531640
b=9
id(b)
140721286531768
c=b-4
c
5
id(c)
140721286531640
b=b-4
b
5
id(b)
140721286531640
import builtins
dir(builtins)

n1=20
n2=22
n3=4
n1+n3
24
n1-n2
-2
n2-n1
2
id(5)
140721286531640
id(a)
140721286531640
n1*n3
80
n1/n3
5.0
n1//n3
5
n2%n3
2
n1%n2
20
20+4
24
2**3
8
2**3**2
512
2**(1/2)
1.4142135623730951
2**(1/3)
1.2599210498948732
"likitha"*3
'likithalikithalikitha'
3*"likitha"
'likithalikithalikitha'
z='apple'
z=7
z
7
'twenty'+4
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    'twenty'+4
TypeError: can only concatenate str (not "int") to str
a=int()
a
0
b=int(7)
b
7
c=int('9')
c
9
d=int('101',2)
>>> d
5
>>> e
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> e=int('132',2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    e=int('132',2)
ValueError: invalid literal for int() with base 2: '132'
>>> e=int('132',10)
>>> e
132
>>> d=int('101',3)
>>> d
10
>>> d=int('101',4)
>>> d
17
>>> f=int('789')
>>> f
789
