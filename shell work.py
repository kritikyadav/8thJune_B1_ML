Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======================= RESTART: D:/z record/ML/day 9/script_file.py =======================
>>> print(d)
{'name': 'Rahul', 'age': 23}
>>> 
======================= RESTART: D:/z record/ML/day 9/script_file.py =======================
{'name': 'Rahul', 'age': 23}
>>> s={i for i in a}
>>> set(a)
{'name', 'age'}
>>> g=(i for i in a)
>>> g
<generator object <genexpr> at 0x0000023F937CD580>
>>> az=[chr(i):ord(i) for i in range(97,123)]
SyntaxError: invalid syntax
>>> az=[{chr(i):ord(i)} for i in range(97,123)]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    az=[{chr(i):ord(i)} for i in range(97,123)]
  File "<pyshell#6>", line 1, in <listcomp>
    az=[{chr(i):ord(i)} for i in range(97,123)]
TypeError: ord() expected string of length 1, but int found
>>> az=[chr(i),ord(i) for i in range(97,123)]
SyntaxError: invalid syntax
>>> az=[chr(i),i for i in range(97,123)]
SyntaxError: invalid syntax
>>> az=[chr(i) for i in range(97,123)]
>>> az
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> 
======================= RESTART: D:/z record/ML/day 9/script_file.py =======================
(0, 3)
(1, 5)
(2, 7)
(3, 2)
(4, 8)
(5, 3)
(6, 9)
>>> 
======================= RESTART: D:/z record/ML/day 9/script_file.py =======================
>>> print(c)
{'name': ['Rahul', 'vijay', 'vishal'], 'age': [20, 21, 22]}
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
>>> print(content)
name,age,subject
sujeet,20,python
vineet,21,python
ajay,22,java
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
name,age,subject
sujeet,20,python
vineet,21,python
ajay,22,java
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
name,age,subject
sujeet,20,python
vineet,21,python
ajay,22,java
['name,age,subject', 'sujeet,20,python', 'vineet,21,python', 'ajay,22,java']
>>> content
'name,age,subject\nsujeet,20,python\nvineet,21,python\najay,22,java'
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
name,age,subject
sujeet,20,python
vineet,21,python
ajay,22,java
['name,age,subject', 'sujeet,20,python', 'vineet,21,python', 'ajay,22,java']
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
['name,age,subject', 'sujeet,20,python', 'vineet,21,python', 'ajay,22,java']
['name', 'age', 'subject']
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
['name,age,subject', 'sujeet,20,python', 'vineet,21,python', 'ajay,22,java']
['name', 'age', 'subject']
Traceback (most recent call last):
  File "D:/z record/ML/day 9/script_file.py", line 32, in <module>
    print(row)
NameError: name 'row' is not defined
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
['name,age,subject', 'sujeet,20,python', 'vineet,21,python', 'ajay,22,java']
['name', 'age', 'subject']
[['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
>>> heading
['name', 'age', 'subject']
>>> row
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    row
NameError: name 'row' is not defined
>>> rows
[['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
>>> heading
['name', 'age', 'subject']
>>> data=[ [row[i] for row in rows] for i,v in enumerate(heading) ]
>>> data
[['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
['name', 'age', 'subject']
[['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
[['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
>>> 
>>> 
>>> alldata=list(zip(*rows))
>>> alldata
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]
>>> 
>>> zip(heading,alldata)
<zip object at 0x000001F6E8AEC540>
>>> list(zip(heading,alldata))
[('name', ('sujeet', 'vineet', 'ajay')), ('age', ('20', '21', '22')), ('subject', ('python', 'python', 'java'))]
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]
{'name': ('sujeet', 'vineet', 'ajay'), 'age': ('20', '21', '22'), 'subject': ('python', 'python', 'java')}
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]


{'name': ('sujeet', 'vineet', 'ajay'), 'age': ('20', '21', '22'), 'subject': ('python', 'python', 'java')}
>>> 
================= RESTART: D:/z record/ML/day 9/script_file.py =================
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]
data
new data
{'name': ('sujeet', 'vineet', 'ajay'), 'age': ('20', '21', '22'), 'subject': ('python', 'python', 'java')}
>>> 
================================= RESTART: D:/z record/ML/day 9/script_file.py =================================
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
alldata
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]
data
new data
{'name': ('sujeet', 'vineet', 'ajay'), 'age': ('20', '21', '22'), 'subject': ('python', 'python', 'java')}
>>> 
================================= RESTART: D:/z record/ML/day 9/script_file.py =================================
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
alldata
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]
data
data
new data
{'name': ('sujeet', 'vineet', 'ajay'), 'age': ('20', '21', '22'), 'subject': ('python', 'python', 'java')}
>>> 
================================= RESTART: D:/z record/ML/day 9/script_file.py =================================
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
alldata
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]
data
[('name', ('sujeet', 'vineet', 'ajay')), ('age', ('20', '21', '22')), ('subject', ('python', 'python', 'java'))]
new data
{'name': ('sujeet', 'vineet', 'ajay'), 'age': ('20', '21', '22'), 'subject': ('python', 'python', 'java')}
>>> 
>>> 
================================= RESTART: D:/z record/ML/day 9/script_file.py =================================
content
 name,age,subject
sujeet,20,python
vineet,21,python
ajay,22,java
clist
 ['name,age,subject', 'sujeet,20,python', 'vineet,21,python', 'ajay,22,java']
heading
 ['name', 'age', 'subject']
rows
 [['sujeet', '20', 'python'], ['vineet', '21', 'python'], ['ajay', '22', 'java']]
data
 [['sujeet', 'vineet', 'ajay'], ['20', '21', '22'], ['python', 'python', 'java']]
alldata
[('sujeet', 'vineet', 'ajay'), ('20', '21', '22'), ('python', 'python', 'java')]
data
[('name', ('sujeet', 'vineet', 'ajay')), ('age', ('20', '21', '22')), ('subject', ('python', 'python', 'java'))]
new data
{'name': ('sujeet', 'vineet', 'ajay'), 'age': ('20', '21', '22'), 'subject': ('python', 'python', 'java')}
>>> 