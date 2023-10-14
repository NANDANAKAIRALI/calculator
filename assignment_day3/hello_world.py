import tkinter

window=tkinter.Tk()
window.title("HELLO")
window.minsize(600,500)

label=tkinter.Label(text="NAMASTE..",font=('Times New Roman',24))
label.grid(row=0,column=0, padx=10, pady=10)

window.mainloop()

