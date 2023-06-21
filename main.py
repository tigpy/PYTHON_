
print("hello") 
print ("changing \"value of a\" \n variable assigning")
for i in range(1,23):
    print(i)
def add_numbers(a,b):
    return a+b
result  = add_numbers(56,79)
print(result) 
my_list=[1,2,3,4,5,6,7]
print(my_list[0])
my_list.append(8)
print(my_list)
my_dict={"name":"Aryan","age":19,"Location":"mumbai"}
print(my_dict["name"])
my_dict["age"]=19
print(my_dict)
 
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
        def say_hello(self):
            print(f"hello, my name is {self.name} and i'm {self.age} years old")
            person = person("aryan",19)
            person.say_hello()

            
import tkinter as tk

def button_click():
    label.config(text="You are dumb!")


window = tk.Tk()
window.title("My App")


label = tk.Label(window, text="Click the button!")
label.pack()


button = tk.Button(window, text="Yes!", command=button_click)
button.pack()
button = tk.Button(window, text="NO!", command=button_click)
button.pack()




window.mainloop()