superhero=input("what is your superpower? ")
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
second=input("enter youe second number: ")

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

number=range(5)
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

