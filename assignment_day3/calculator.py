import tkinter

window=tkinter.Tk()
window.title("CALCULATOR")
window.minsize(200,350)
def print_button1():
    text_print.insert(tkinter.END,"1")
def print_button2():
    text_print.insert(tkinter.END,"2")
def print_button3():
    text_print.insert(tkinter.END,"3")
def print_button4():
    text_print.insert(tkinter.END,"4")
def print_button5():
    text_print.insert(tkinter.END,"5")
def print_button6():
    text_print.insert(tkinter.END,"6")
def print_button7():
    text_print.insert(tkinter.END,"7")
def print_button8():
    text_print.insert(tkinter.END,"8")
def print_button9():
    text_print.insert(tkinter.END,"9")
def print_button0():
    text_print.insert(tkinter.END,"0")
def print_dot():
    text_print.insert(tkinter.END,".")
def print_add():
    text_print.insert(tkinter.END,"+")
def print_sub():
    text_print.insert(tkinter.END,"-")
def print_mul():
    text_print.insert(tkinter.END,"*")
def print_div():
    text_print.insert(tkinter.END,"/")
def equal_button():
     result = eval(text_print.get())
     text_print.delete(0, tkinter.END)
     text_print.insert(0,result)
def clear_button():
    text_print.delete(0,tkinter.END)


text_print=tkinter.Entry()
text_print.grid(row=0, column=0, columnspan=3,sticky="nsew")
b1=tkinter.Button(text="1",command=print_button1)
b1.grid(row=3, column=0, sticky="nsew")
b2=tkinter.Button(text="2",command=print_button2)
b2.grid(row=3, column=1, sticky="nsew")
b3=tkinter.Button(text="3",command=print_button3)
b3.grid(row=3, column=2, sticky="nsew")
b4=tkinter.Button(text="4",command=print_button4)
b4.grid(row=2, column=0, sticky="nsew")
b5=tkinter.Button(text="5",command=print_button5)
b5.grid(row=2, column=1, sticky="nsew")
b6=tkinter.Button(text="6",command=print_button6)
b6.grid(row=2, column=2, sticky="nsew")
b7=tkinter.Button(text="7",command=print_button7)
b7.grid(row=1, column=0, sticky="nsew")
b8=tkinter.Button(text="8",command=print_button8)
b8.grid(row=1, column=1, sticky="nsew")
b9=tkinter.Button(text="9",command=print_button9)
b9.grid(row=1, column=2,sticky="nsew")
b0=tkinter.Button(text="0",command=print_button0)
b0.grid(row=4, column=2,sticky="nsew")
b_dot=tkinter.Button(text=".",command=print_dot)
b_dot.grid(row=4, column=1,sticky="nsew")
b_plus=tkinter.Button(text="+",command=print_add)
b_plus.grid(row=1, column=3,sticky="nsew")
b_minus=tkinter.Button(text="-",command=print_sub)
b_minus.grid(row=2, column=3, sticky="nsew")
b_mul=tkinter.Button(text="*",command=print_mul)
b_mul.grid(row=3, column=3,sticky="nsew")
b_div=tkinter.Button(text="/",command=print_div)
b_div.grid(row=4, column=3, sticky="nsew")
b_equal=tkinter.Button(text="=",command=equal_button)
b_equal.grid(row=0, column=3,sticky="nsew")
bC=tkinter.Button(text="C",command=clear_button)
bC.grid(row=4, column=0, sticky="nsew")

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.mainloop()


