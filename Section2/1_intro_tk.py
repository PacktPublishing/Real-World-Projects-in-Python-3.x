from tkinter import *

# the first thing you need is a window or root
 
window = Tk()
#widgets get instaniated and later placed in the window
label = Label(window, text="Welcome to Refi Analyze")
text = Text(window, cnf={'bg':'red'})
button = Button(window, text="click me!")

# when ready you place objects (widgets) in the window
# you place in either pack: centered
# or grid --> define how many columns and rows
# you can also .place widgets with x,y coords
label.pack()
text.pack()
button.pack()

# you must always call the main loop to 
# to render GUI
window.mainloop()

