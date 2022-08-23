import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

label = tk.Label(text="Password generator")
label.pack(side="top")

val1 = tk.IntVar()
val2 = tk.IntVar()
val3 = tk.IntVar()

checkbox1 = tk.Checkbutton(text="Use capital letters")
checkbox2 = tk.Checkbutton(text="Use digits")
checkbox3 = tk.Checkbutton(text="Use special characters")

checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

button = tk.Button(text="Generate!")
button.pack()

password = tk.Entry()
password.pack()

root.mainloop()
