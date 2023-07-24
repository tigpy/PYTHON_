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
