#true False
print(5==5)
print(5 > 5)
#none
print(None==0)   
print(None==False)
print(None== [])
print(None==None)

def a_void_function():
    a=1
    b=2
    c=a * b
    
x = a_void_function()
print(x)

#and or not
print(True and False)
print(True or False)
print(not False)
print(True and True)
print(True or True)
print(not True)

#as
import math as myMath
print(myMath.tan(myMath.pi))

#assert
assert 5>4
assert 5==5
#no output will come bcs both condition is true.

#break
for i in range(1,11):
 if i == 8:
    break
 print(i)

 #continue
 for i in range(1,8):
    if i == 5:
       continue
    print(i)

    #class
class ExampleClass:
       def function1(parameters):
          print("function1() executing...")
          def function2(parameters):
             print("function2() executing...")
             ob1 = ExampleClass()
             ob1.function1()
             ob1.function2()


#def
def function_name(parameters):
   pass
function_name(9) #no output here bcs pass don't produce output

#del
a = 19
print(a)
del a #error bcs a got deleted

#if...elif...else
num = 3
if num == 1:
   print("one")
elif num == 2:
   print("Two")
else:
   print("something else")

   #try...raise...catch...finally
   try:
      x=9
      raise ZeroDivisionError
   except ZeroDivisionError:
      print("Division cannot be performed")
   finally:
      print("Execution Successfully")

#for
for i in range(1,10):
   print(i)

#from... import 
import math
from math import cos
print(cos(10))

#global
globvar = 10
def read1():
   print(globvar)
def write1():
   global globvar
   globvar=6
def write2():
   globvar = 15
read1()
write1()
read1()
write2()
read1()

#in 
a=[1,2,3,4]
print(4 in a)
print(44 in a)
print(4 not in a)

#is 
print(True is True)

# lambda
a = lambda x: x*3
for i in range (1,11):
   print(a(i))

#nonlocal
def outer_function():
   a=6
   def inner_function():
      nonlocal a
      a=10
      print("inner function: ",a)
      inner_function()
   print("outer function: ",a) 
outer_function()

#pass
def function(args):
   pass
function(10)

#return
def func_return():
   a=10
   return a
print(func_return())

#while
i = 5
while(i>0):
   print(i)
   i-=1

#with
with open('example.txt', 'w') as my_file:
   my_file.write('hello aryan')

#yield
def generator():
   for i in range(6):
      yield i*i
g = generator()
for i in g:
   print(i)