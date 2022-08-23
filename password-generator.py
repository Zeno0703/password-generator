import random
import string
import tkinter as tk

abcLowercase = list(string.ascii_lowercase)
abcUppercase = list(string.ascii_uppercase)
numbers = list(string.digits)
specialCharacters = list(string.punctuation)

root = tk.Tk()
root.geometry("400x400")

label = tk.Label(text="Password generator")
label.pack(side="top")

sliderVal = tk.IntVar()

slider = tk.Scale(from_=8, to=16, orient="horizontal", variable=sliderVal)
slider.pack()

val1 = tk.IntVar()
val2 = tk.IntVar()
val3 = tk.IntVar()

checkbox1 = tk.Checkbutton(text="Use capital letters", onvalue=1, offvalue=0, variable=val1)
checkbox2 = tk.Checkbutton(text="Use digits", onvalue=1, offvalue=0, variable=val2)
checkbox3 = tk.Checkbutton(text="Use special characters", onvalue=1, offvalue=0, variable=val3)

checkbox1.pack()
checkbox2.pack()
checkbox3.pack()


def addTickedBoxes(standard):

    if val1.get() == 1:
        standard.append(abcUppercase)

    if val2.get() == 1:
        standard.append(numbers)

    if val3.get() == 1:
        standard.append(specialCharacters)


def generatePassword():

    password = ""
    alphabetArray = [abcLowercase]
    addTickedBoxes(alphabetArray)
    passwordLength = sliderVal.get()

    for i in range(passwordLength):
        alphabet = alphabetArray[random.randint(0, len(alphabetArray) - 1)]
        password += alphabet[random.randint(0, len(alphabet) - 1)]

    return password


def displayPassword():
    entry.delete(0, 17)
    password = generatePassword()
    entry.insert(0, password)


button = tk.Button(text="Generate!", command=displayPassword)
button.pack()

entry = tk.Entry()
entry.pack()

root.mainloop()
