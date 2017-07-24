Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 10
>>> a = b
>>> b = a
>>> clear
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> a = 5
>>> b = 10
>>> c = a
>>> a = b
>>> b = c
>>> a
10
>>> b
5
>>> four = '4'
>>> print four*3
SyntaxError: Missing parentheses in call to 'print'
>>> print (four*3)
444
>>> my_name= 'sh'
>>> print ('hi," + myname')
hi," + myname
>>> my_name= 'shmuel'
>>> print('hi' + my_name)
hishmuel
>>> print('hi'+  my_name)
hishmuel
>>> my_name= ' shmuel'
>>> print('hi' +my_name)
hi shmuel
>>> my_age= 15
>>> print ('i am ' + my_age + 'years old')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print ('i am ' + my_age + 'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> my_age= ' 15'
>>> print('i am' +my_age + "years old")
i am 15years old
>>>  print('i am' +my_age + " years old")

SyntaxError: unexpected indent
>>> my_age = 15
>>> score = 1
>>> total = score + (count * 2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    total = score + (count * 2)
NameError: name 'count' is not defined
>>> print(total)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
>>> score = '1'
>>> count = score
>>> total = score + (count * 2)
>>> print(total)
111
>>> score = 1
>>> count = score
>>> total = score + (count * 2)
>>> print (total)
3
>>> 
