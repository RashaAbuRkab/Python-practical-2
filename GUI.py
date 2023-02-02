from bankaccount import BankAccount
from tkinter import *

harrysAccount = BankAccount(1000.0)

master = Tk()

def deposite():
    amount = float(entreyvalue.get())
    harrysAccount.deposit(amount)
    
def getBalance():
    balancevalue.config(text = "Balance is:" + str(harrysAccount.getBalance()))    
    
def withdraw():
    amount = float(entreyvalue.get())
    harrysAccount.withdraw(amount)
    
def addInterest():
    amount = float(entreyvalue.get())
    harrysAccount.addInterest(amount)

topframe = Frame(master)
topframe.pack()
enter_label = Label(topframe,text = "Enter Value")
enter_label.pack(side=LEFT)

entreyvalue = DoubleVar()
theAmount = Entry(topframe,bd=5,textvariable = entreyvalue)
theAmount.pack(side=LEFT)

midframe = Frame(master)
midframe.pack()
depositeButton = Button(midframe,text="deposite",command = lambda: deposite())
depositeButton.pack(side=LEFT)

withdrawButton = Button(midframe,text="withdraw",command= lambda:withdraw())
withdrawButton.pack(side=LEFT)

addinterestButton = Button(midframe,text="add interest",command=lambda:addInterest())
addinterestButton.pack(side=LEFT)

getbalanceButton = Button(midframe,text="get Balance",command=lambda:getBalance())
getbalanceButton.pack(side=LEFT)

bottomframe = Frame(master)
bottomframe.pack()

balancevalue = Label(bottomframe,text="Balance is: ")
balancevalue.pack()
master.mainloop()




