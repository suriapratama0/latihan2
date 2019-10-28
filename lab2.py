Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input(masukan nilai a:"))
	
SyntaxError: invalid syntax
>>> a=input("masukan nilai a:")
masukan nilai a:20
>>> b=input(masukan nilai b:")
	
SyntaxError: invalid syntax
>>> b=input("masukan nilai b:")
masukan nilai b:20
>>> print("variable a=",a)
variable a= 20
>>> print("variable b=",b)
variable b= 20
>>> print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))
TypeError: %d format: a number is required, not str
>>> print("hasil penggabungan {1}&{0}=%d".format(20,20) %(20+20))
hasil penggabungan 20&20=40
>>> #konversi nilai variable
>>> a=int(a)
>>> b=int(b)
>>> print("hasil penjumlahan {1}+{0}=%d".format(20,20) %(20+20))
hasil penjumlahan 20+20=40
>>> print("hasil pembagian {1}/{0}=%d".format(20,20) %(20/20))
hasil pembagian 20/20=1
>>> 
