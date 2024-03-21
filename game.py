from tkinter import *
from tkinter.scrolledtext import *
import random

class Game:
    def __init__(self):
        self._win=Tk()
        self._win.title('Hi Lo Game')
        
        #self._win.geometry('300x200')
        #call a method to create widgets
        self.createWidgets()
        
        self._win.mainloop()
    
    def createWidgets(self):
        self._lblGuess = Label(text='Enter Guess:')
        self._lblMode = Label(text='Mode')
        self._txtName = Entry(width=10)
        self._btnStart = Button(text='Start',command=self.btnClick)
        self._btnGuess = Button(text='Guess',command=self.guess,state=DISABLED)
        self._lblOutput = Label()
        self._sclOutput = ScrolledText(width=25,height=50,state=DISABLED)
        #create radio buttons
        f=Frame()
        #group the 2 radio buttons
        self._rbtn = IntVar() #this is an integer object
        self._rbtnEasy =Radiobutton(f,text='Easy',variable=self._rbtn,value=1)
        self._rbtnDifficult=Radiobutton(f,text='Difficult',variable=self._rbtn,value=0)

        #Layout the widgets using grid layout
        self._lblMode.grid(row=0,column=0,sticky=W)
        f.grid(row=0,column=1)
        self._btnStart.grid(row=0,column=3,sticky=EW)

        self._lblGuess.grid(row=1,column=0)
        self._txtName.grid(row=1,column=1)
        self._btnGuess.grid(row=1,column=3)
        
        self._lblOutput.grid(row=3,column=0,columnspan=2,sticky=W)
        #place the radio buttons
        self._rbtnEasy.grid(row=0,column=0)
        self._rbtnDifficult.grid(row=0,column=1)
        
        self._sclOutput.grid(row=4,column=0,columnspan=4)

    
    def btnClick(self):
        self._btnStart.configure(state=DISABLED)
        self._btnGuess.configure(state=NORMAL)
        self._sclOutput.delete('1,0',END) 
        if self._rbtn.get() ==1:
            self._guessNum=random.randint(0,100)
        else:
            self._guessNum=random.randint(0,50)
        guessInput=int(self._txtName.get())
        while guessInput != self._guessNum:
            self.guess()

    def guess(self):
        print(self._guessNum)
        guessInput=int(self._txtName.get())
        self._txtName.delete(0, 'end')
        if guessInput > self._guessNum:
            self._sclOutput.configure(state=NORMAL)
            self._sclOutput.insert(END,f'{guessInput} is too high!\n')
            self._sclOutput.configure(state=DISABLED)
        elif guessInput< self._guessNum:
            self._sclOutput.configure(state=NORMAL)
            self._sclOutput.insert(END,f'{guessInput} is too low!\n')
            self._sclOutput.configure(state=DISABLED)
        else:
            self._sclOutput.configure(state=NORMAL)
            self._sclOutput.insert(END,f'{guessInput} is correct!\n')
            self._sclOutput.configure(state=DISABLED)   
            self._btnStart.configure(state=NORMAL)
            self._btnGuess.configure(state=DISABLED)




gui = Game()