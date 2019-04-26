from tkinter import *

def doOK():
    print("OK was clicked")

def doCancel():
    print("Cancel was clicked")
    
   

window = Tk()
btnOK = Button(window, text="OK", fg="blue", command=doOK)
btnCancel = Button(window, text="cancel", bg="red", command=doCancel)


btnOK.grid(row=1,column=1, padx =(2, 10), pady=5) # show formatting second

btnCancel.place(x=72, y=5)

window.mainloop()
