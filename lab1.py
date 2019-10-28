Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # penggunaan end
>>> print('A', end='')
A
>>> print('B', end='')
B
>>> print('C', end='')
C
>>> print()

>>> print('X')
X
>>> print('Y')
Y
>>> print('Z')
Z
>>> 
>>> # penggunaan separator
>>> w, x, y, z = 10, 15, 20, 25
>>> print(w, x ,y, z)
10 15 20 25
>>> print(w, x, y, z, sep=',')
10,15,20,25
>>> print(w, x, y, z, sep='')
10152025
>>> print(w, x, y, z, sep=':')
10:15:20:25
>>> print(w, x, y, z, sep='.....')
10.....15.....20.....25
>>> 
>>> # string format
>>> print(0, 10**0)
0 1
>>> print(1, 10**1)
1 10
>>> print(2, 10**2)
2 100
>>> print(3, 10**3)
3 1000
>>> print(4, 10**4)
4 10000
>>> print(5, 10**5)
5 100000
>>> print(6, 10**6)
6 1000000
>>> print(7, 10**7)
7 10000000
>>> print(8, 10**8)
8 100000000
>>> print(9, 10**9)
9 1000000000
>>> print(10, 10**10)
10 10000000000
>>> 
>>> # string format
>>> print('{0:>3} {1:>16}'.format{0, 10**0))
SyntaxError: invalid syntax
>>> print('{0:>3} {1:>16}'.format(0, 10**0))
  0                1
>>> print('{0:>3} {1:>16}'.format{1, 10**1))
SyntaxError: invalid syntax
>>> print('{0:>3} {1:>16}'.format(1, 10**1))
  1               10
>>> print('{0:>3} {1:>16}'.format(2, 10**2))
  2              100
>>> print('{0:>3} {1:>16}'.format(3, 10**3))
  3             1000
>>> print('{0:>3} {1:>16}'.format(4, 10**4))
  4            10000
>>> print('{0:>3} {1:>16}'.format(5, 10**5))
  5           100000
>>> print('{0:>3} {1:>16}'.format(6, 10**6))
  6          1000000
>>> print('{0:>3} {1:>16}'.format(7, 10**7))
  7         10000000
>>> print('{0:>3} {1:>16}'.format(8, 10**8))
  8        100000000
>>> print('{0:>3} {1:>16}'.format(9, 10**9))
  9       1000000000
>>> print('{0:>3} {1:>16}'.format(10, 10**10))
 10      10000000000
>>> 
#latihan2
# latihan2
