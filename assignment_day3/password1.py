import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    password_list = []
    for i in range(0, int(no_letter.get())):
        password_list += random.choice(letters)

    for i in range(0,int(no_sym.get()) ):
        password_list += random.choice(symbols)

    for i in range(0,int(no_numb.get())):
        password_list += random.choice(numbers)

    random.shuffle(password_list)


    password = ""
    for i in password_list:
        password += i
    label4.config(text=f"{password}")
    


import tkinter

window=tkinter.Tk()
window.title("PASSWORD")
window.minsize(600,500)

label=tkinter.Label(text="WELCOME TO THE PASSWORD GENERATOR")
label.grid(row=0,column=0, padx=10, pady=10)
label1=tkinter.Label(text="NUMBER OF LETTERS")
label1.grid(row=1,column=0, padx=10, pady=10)
no_letter=tkinter.Entry()
no_letter.grid(row=1, column=1, padx=10, pady=10)
label2=tkinter.Label(text="NUMBER OF NUMBERS ")
label2.grid(row=2,column=0, padx=10, pady=10)
no_numb=tkinter.Entry()
no_numb.grid(row=2, column=1, padx=10, pady=10)
label3=tkinter.Label(text="NUMBER OF SYMBOLS")
label3.grid(row=3,column=0, padx=10, pady=10)
no_sym=tkinter.Entry()
no_sym.grid(row=3, column=1, padx=10, pady=10)
b2=tkinter.Button(text="SUBMIT",command=password_generator)
b2.grid(row=3, column=3, padx=10, pady=10)
label4=tkinter.Label(text=" ")
label4.grid(row=4,column=0, padx=10, pady=10)

window.mainloop()