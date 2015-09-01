Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "ce"
ce
>>> print 2
2
>>> a=2
>>> print a+3
5
>>> a = raw_input("Masukkan kalimat ")
Masukkan kalimat jack
>>> a
'jack'
>>> print a
jack
>>> b = raw_input("Input 2 : ")
Input 2 : clelel
>>> print a + b
jackclelel
>>> print a - b

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print a - b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a + b
'jackclelel'
>>> print "ini adalah {0}".format(a)
ini adalah jack
>>> 
