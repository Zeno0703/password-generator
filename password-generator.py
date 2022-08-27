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
label.pack(side="top", fill="both")

sliderVal = tk.IntVar()

slider = tk.Scale(from_=8, to=16, orient="horizontal", variable=sliderVal)
slider.pack(fill="both")

val1 = tk.IntVar()
val2 = tk.IntVar()
val3 = tk.IntVar()

checkbox1 = tk.Checkbutton(text="Use capital letters", onvalue=1, offvalue=0, variable=val1)
checkbox2 = tk.Checkbutton(text="Use digits", onvalue=1, offvalue=0, variable=val2)
checkbox3 = tk.Checkbutton(text="Use special characters", onvalue=1, offvalue=0, variable=val3)

checkbox1.pack(fill="both")
checkbox2.pack(fill="both")
checkbox3.pack(fill="both")


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
        letter = alphabet[random.randint(0, len(alphabet) - 1)]

        if password.count(letter) >= 2:
            letter = alphabet[random.randint(0, len(alphabet) - 1)]

        password += letter

    return password


def displayPassword():
    entry.delete(0, sliderVal.get() + 1)
    entry.insert(0, generatePassword())


button = tk.Button(text="Generate!", command=displayPassword)
button.pack(fill="both")

entry = tk.Entry()
entry.pack(fill="both")

root.mainloop()
