from tkinter import *
master = Tk()

def sum_the_numbers():
    num1 = float(entry_value1.get())
    num2 = float(entry_value2.get())
    result = num1+num2
    the_result.config(text = "the Result is: "+str(result))

topframe = Frame(master)
topframe.pack()
num1_label = Label(topframe,text = "Enter first number")
num1_label.pack(side=LEFT)
entry_value1 = DoubleVar()
num1_Entry = Entry(topframe,bd  = 5, textvariable = entry_value1)
num1_Entry.pack(side=LEFT)

midframe = Frame(master)
midframe.pack()
num2_label = Label(midframe,text = "Enter second number")
num2_label.pack(side=LEFT)
entry_value2 = DoubleVar()
num2_Entry = Entry(midframe,bd  = 5, textvariable = entry_value2)
num2_Entry.pack(side=LEFT)

thirdframe = Frame(master)
thirdframe.pack()
sum_button = Button(thirdframe,text="Sum the numbers",command = lambda: sum_the_numbers())
sum_button.pack()

lastframe = Frame(master)
lastframe.pack()
the_result = Label(lastframe)
the_result.pack()
master.mainloop()