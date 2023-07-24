superhero = input("what is your superpower? ")
print(superhero)
print("hello" + superhero)

old_age=input("enter your old age? ")
int(old_age)
new_age=int(old_age)+2
print(new_age)
print(float(18))
first=input("enter first number? ")
second=input("enter second number? ")
sum=int(first)+int(second)
print("The sum is:" + str(sum))
name="aryan singh"
print(name.lower())
print(name.find('singh'))
print(name.replace("singh","ajay singh"))
print("t" in name)
print(5//2)
print(5%2)
print(5**2)
i=2
# i=i+2
i+=2
print(i)
print(3>2 and 2>1)
print(2>3  or 2>1)
# negation
print(not 3>2)
# ifelse
age=2
if age>=18:
       print("you are adult")
       print("you can vote")
elif age<18 and age>3:
       print("your in school")
else:
       print("you are a child")


print("thanks")
#lets make a calculator
first=input("enter your first number: ")
operator=input("enter operator(+,-,*,/,%:)")
second=input("enter your second number: ")

first=int(first)
second=int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("invalid operation")

number = range(5)
print(number)
#loop
i=1
while i<=5:
    print(i * "*")
    i=i+1
i=5
while i>=0:
    print(i * "*")
    i=i-1


for item in range(6):
    print(item + 1)

#List
marks = [95,98,97]
print(marks[1:3])

for score in marks:
    print(score)
marks.append(99.54)
marks.insert(0,99)
print(marks)
print(99 in marks)
print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
marks.clear()
print(marks)

#break and continue

students = ["aryan", "himanshu", "shubham", "piyush", "aniket"]
for student in students:
    if student == "piyush":
        break;
    elif student == "shubham":
        continue

    print(student)

#Tuple
marks = (95, 98, 97, 97, 97)
print(marks.count(97))
print(marks.index(95))
#[],(),{} = list,tuple,sets
person = "ram", "sam", "abhi"
print(person)
#Dictionary
marks = {95, 98, 97, 99}#sets don't have index (unordered)
for score in marks:
    print(score)
marks = {"english" : 95, "chemistry" : 96}
print(marks["chemistry"])
marks["physics"] = 97;
print(marks)

marks["physics"] = 99;
print(marks)

#Functions
#1. In-built Function
int(), bool(), str()

#2. Module Function
import math
print(dir(math))
from math import sqrt
print(sqrt(16))
from math import * #"*" will import all function.
print(sqrt(78))
#3. User-defined function
def print_sum(first, second=4):
    print(first + second)

print_sum(1)


















