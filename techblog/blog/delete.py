from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!")

#Displaying on screen
# myLabel.pack()
# myLabel.grid(row=0, column=0) #, columnspan=3

#Title
#root.title("Simple") #changing title
#Buttons
#Disabled button
#myButton = Button(root, text="Click me", state=DISABLED)
#Longer and highter button
#myButton = Button(root, text="Click me", padx=50, pady=50)
#Displaying
#myButton.pack()
#Writing smth after click
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a Button")
#     myLabel.pack()
#
# myButton = Button(root, text="Click me", command=myClick, fg='blue', bg='red')
# myButton.pack()

# e = Entry(root, width = 50) #fg, bg - color works, borderwidth = 50 -
# e.get() - get this input
#e.insert - text inside input box
# e.pack()


root.mainloop()