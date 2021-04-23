0
>>> src = 'files/'
>>> for i in range(1, 101):
... file = open(src+str(i)+'.txt', 'w')
  File "<stdin>", line 2
    file = open(src+str(i)+'.txt', 'w')
    ^

>>> for i in range(1, 101):
...   file = open(src+str(i)+'.txt', 'w')
...   file.close()
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'files/1.txt'
>>> for i in range(1, 101):
... import os
  File "<stdin>", line 2
    import os
    ^
>>> os.mkdir('files')
>>> for i in range(1, 101):
...   file = open(src+str(i)+'.txt', 'w')
...   file.close()
...
>>> for i in range(1, 101):
...  os.remove(src+str(i)+'.txt')
...
>>>