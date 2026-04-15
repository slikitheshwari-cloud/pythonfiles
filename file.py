Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(M:\1st semester)
SyntaxError: invalid syntax
>>> print("M:\1st semester")
M:st semester
>>> print("M:\1st semester\today\no1>txt")
M:st semester	oday
o1>txt
>>> print(r"M:\1st semester\today\no1>txt")
M:\1st semester\today\no1>txt
>>> print(r"M:\1st semester\demo1.txt","w")
M:\1st semester\demo1.txt w
>>> fp=open(r"M:\1st semester\demo1.txt","w")
>>> temp="today is monday.Sports day as well as regular classes."
>>> fp.write(temp)
54
>>> f[=open(r"M:\1st semester\demo1.txt","w")
...   
SyntaxError: invalid syntax
>>> fp=open(r"M:\1st semester\demo1.txt","w")
...   
>>> temp="today is monday.Sports day as well as regular classes."
...   
fpfp.write(temp)
  
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fpfp.write(temp)
NameError: name 'fpfp' is not defined
fp.write(temp)
  
54
fp.write("Thanks.you")
  
10
fp.close()
  
fp=open(r"M:\1st semester\demo1.txt","w")
  
fp.write("File handling \n is easy \n but littlw but typica;")
  
48
fp=open(r"M:\1st semester\demo1.txt","w")
  
temp="today is monday.Sports day as well as regular classes."
  
fp.write(temp)
  
54
fp.write("Thanks.you")
  
10
fp.write("File handling \n is easy \n but littlw but typical;")
  
49
fp.close()
  
print(temp)
  
today is monday.Sports day as well as regular classes.
nu=0
  
for i in temp:
  if i in "aeiouAEIOU":
  nv+=1
  
SyntaxError: expected an indented block after 'if' statement on line 2
nv=0
  
for i in temp:
  if i in "aeiouAEIOU":
  nv+=1
  
SyntaxError: expected an indented block after 'if' statement on line 2
for i in temp:
  if i in "aeiouAEIOU":
      nv+=1
print(nv)
  
SyntaxError: invalid syntax
nv=0
  
for i in temp:
  if i in "aeiouAEIOU":
    nv+=1

  
print(nv)
  
15
with open("demo1.txt","w") as file:
  file.write("hello,python\n")
  file.write(:="file havdling is easy.")
  
SyntaxError: invalid syntax
with open("demo1.txt","w") as file:
  file.write("hello,python\n")
  file.write("file havdling is easy.")

  
13
22
with open("notes.txt","r") as file:
  content=file.read()
  print(content)

  
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    with open("notes.txt","r") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'
with open(r"M:\1st semester\demo1.txt","w") as file:
  file.write("hello,python\n")
  file.write("file havdling is easy.")

  
13
22
with open(r"M:\1st semester\notes.txt","r") as file:
  content=file.read()
  print(content)

  

with open(r"M:\1st semester\notes.txt","r") as file:
  content=file.read()

  
print(content)
  

with open("M:\1st semester\notes.txt","r") as file:
  content=file.read()
  print(content)

  
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    with open("M:\1st semester\notes.txt","r") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'M:\x01st semester\notes.txt'

======================== RESTART: M:/1st semester/python/pyfileh.py =======================
Traceback (most recent call last):
  File "M:/1st semester/python/pyfileh.py", line 2, in <module>
    file.seek(0)
NameError: name 'file' is not defined. Did you mean: 'filter'?

======================== RESTART: M:/1st semester/python/pyfileh.py =======================
Traceback (most recent call last):
  File "M:/1st semester/python/pyfileh.py", line 4, in <module>
    print(file.read(5))
NameError: name 'file' is not defined. Did you mean: 'filter'?

======================== RESTART: M:/1st semester/python/pyfileh.py =======================
hello
,pyth
on
fi
Traceback (most recent call last):
  File "M:/1st semester/python/pyfileh.py", line 8, in <module>
    ing
NameError: name 'ing' is not defined. Did you mean: 'int'?

======================== RESTART: M:/1st semester/python/pyfileh.py =======================
hello
,pyth
on
fi
le havdlin
