from tkinter import Tk, Button, Frame, Entry, END, StringVar, Label
from calculator import Calculator

class calc_frame(Frame):
    # frame contains grid ui and functionality for the calculator
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_grid()
        self.winfo_toplevel().title("First Calculator")
        self.tv1 = float #StringVar()
        self.tv2 = float #StringVar()
        self.labeltext = StringVar()
        self.calc = Calculator()
    
    # 10 functions each called by a different button to call calulator options    
    def calcadd(self):
        print(str(self.tv1) + ' + ' + str(self.tv2) + ' = ' + str(self.calc.add(self.tv1,self.tv2)))
    
    def calcdivide(self):
        print(str(self.tv1) + ' / ' + str(self.tv2) + ' = ' + str(self.calc.divide(self.tv1,self.tv2)))

    def calcmultiply(self):
        print(str(self.tv1) + ' x ' + str(self.tv2) + ' = ' + str(self.calc.multiply(self.tv1,self.tv2)))

    def calcsubtract(self):
        print(str(self.tv1) + ' - ' + str(self.tv2) + ' = ' + str(self.calc.subtract(self.tv1,self.tv2)))
        
    def calcexponent(self):
        print(str(self.tv1) + ' ** ' + str(self.tv2) + ' = ' + str(self.calc.exponent(self.tv1,self.tv2)))
        
    def calcsqroot(self):
        print('Square Root of ' + str(self.tv1) + ' = ' + str(self.calc.sqroot(self.tv1)))
        
    def calcfactorial(self):
        print('Factorial of ' + str(self.tv1) + ' = ' + str(self.calc.factor(self.tv1)))
        
    def calclog(self):
        print('Log e of ' + str(self.tv1) + ' = ' + str(self.calc.log(self.tv1)))
        
    def calclog10(self):
        print('Log 10 of ' + str(self.tv1) + ' = ' + str(self.calc.log10(self.tv1)))
        
    def calcperimeter(self):
        print('Perimeter of a Circle with a radius of ' + str(self.tv1) + ' = ' + str(self.calc.circleperimeter(self.tv1)))
 
 
    def on_button(self):
        print(self.tv1)
        print(self.tv2)
        print(self.bname.text)
        print(self.bname.cget('text'))
        self.mathfunc()
        
    def make_grid(self):
        # this function creates the grid with all components
        button_captions = ["+", "/", "x", "-","!","Exp","SQRT","Log E","Log 10","O"]
        board = [] 
        bc = 0
        bname = ''
        tv_1 = StringVar()
        tv_2 = StringVar()
        labeltext=StringVar()
        
        def callback():
            try:
                self.tv1 = float(tv_1.get())
            except:
##            print(self.tv1)
                self.tv1 = 0
            return
           
        def callback2():
            try:
                self.tv2 = float(tv_2.get())
            except:
                self.tv2 = 0
        #    print(self.tv2)
            return
        
        # this adds 10 buttons to a 5x2 grid, 1 for each calulation - assigns the calc dependent on the order
        for y in range(2):
            for x in range(5):
                bname = 'btn'+str(bc)
                if bc == 0:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcadd)
                elif bc == 1:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcdivide)
                elif bc == 2:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcmultiply)
                elif bc == 3:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcsubtract)
                elif bc == 4:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcfactorial)
                elif bc == 5:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcexponent)
                elif bc == 6:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcsqroot)
                elif bc == 7:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calclog)
                elif bc == 8:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calclog10)
                elif bc == 9:
                    self.bname = Button(self, height=4, width=8, text=button_captions[bc], command=self.calcperimeter)
                
                self.bname.text = button_captions[bc]
                self.bname.grid(row=y, column=x)
                row = self.bname
                bc+=1
            board.append(row)
        
        # add in the entry fields and labels with spaces as apprpriate
        SpaceLabel1 = Label(self).grid(row=3,column=1)
        EntryLabel1 = Label(self, text="Figure 1").grid(row=4,column=0)    
        Label1 = Entry(self, textvariable = tv_1,validate="focusout",validatecommand=callback).grid(row=4, column = 1, columnspan = 2)
        SpaceLabel2 = Label(self).grid(row=5,column=1)
        EntryLabel2 = Label(self, text="Figure 2").grid(row=6,column=0)    
        Label2 = Entry(self, textvariable = tv_2,validate="focusout",validatecommand=callback2).grid(row=6, column = 1, columnspan = 2)
        EntryLabel3 = Label(self, text='Figure 2 used for').grid(row=6,column=3,columnspan=2)
        EntryLabel4 = Label(self, text='+,/,x,- operations only').grid(row=7,column=3,columnspan=2)
        #SpaceLabel3 = Label(self).grid(row=7,column=1)
        EntryLabel5 = Label(self, text="Answer").grid(row=8,column=0)    
        AnswerLabel = Label(self, textvariable=labeltext).grid(row=8, column = 1, columnspan=2)
        SpaceLabel4 = Label(self).grid(row=9,column=0)
        

root = Tk()
calc = calc_frame(root)
root.mainloop()