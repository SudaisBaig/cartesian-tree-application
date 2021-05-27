from tkinter import *
from tkinter.ttk import Combobox
from main import *
from tree import CartesianTree

# Brief explanation
# This code makes two forms 
# object of first form (Master Form) is initialized outside the class
# Inside class (Window) second form is intialized 
# widgets for both forms are specified inside the class
# class window also contains functions to handle events of first form
# Proceed function is an important function which makes object of Cartesian Tree and passes it the list of covidDataNodes = [] 
# as parameter which was initialized in main.py
# once cartesian tree is generated, the method of priority queue is called which is also defined inside the class 
# of cartesian tree. 
# the sorted array of nodes returned by priority queue is then presented by the second form.

col_names = ["Country","Region","Confirmed Cases", "Deaths", "Recovered", "Active", "Incident Rate", "Fatality Ratio"]

class Window:
    def openNewWindow(self,window,sortedList):
        sortedList.insert(0,col_names)  #   For col headings of table
        
        newWindow = Toplevel(window)
        
        newWindow.title("Results")
        newWindow.geometry("1500x700")


        for row in range(self.top+1):
            color = 'blue'
            myfont = ('Arial',9)
            if row == 0:
                color = 'black'
                myfont = ('Helvetica', 10, 'bold')


            for j in range(8):
                self.e = Entry(newWindow, width=20, fg=color,
                                font=myfont)

                self.e.grid(row=row, column=j)
                
                if row == 0:
                    self.e.insert(END, sortedList[row][j])
                    
                if row >= 1:
                    if j == 0:
                        self.e.insert(END, sortedList[row].country)
                    elif j == 1:
                        self.e.insert(END, sortedList[row].region)
                    elif j == 2:
                        self.e.insert(END, sortedList[row].confirmed)
                    elif j == 3:
                        self.e.insert(END, sortedList[row].deaths)
                    elif j == 4:
                        self.e.insert(END, sortedList[row].recovered)
                    elif j == 5:
                        self.e.insert(END, sortedList[row].active)
                    elif j == 6:
                        self.e.insert(END, sortedList[row].incidentRate)
                    elif j == 7:
                        self.e.insert(END, sortedList[row].fatalityRatio)
        
        
        


    def __init__(self, window):

    # add widgets here
        self.window= window
        self.index = 1
        self.max = True
        self.top = 45
        self.btn=Button(window, text="Proceed", fg='black', bg='light green', command=self.proceed)
        self.btn.place(x=480, y=350)

        self.lbl=Label(window, text="Select the Category", fg='Black', font=("Helvetica", 14))
        self.lbl.place(x=30, y=30)

        self.v0=IntVar()
        self.v0.set(1)
        self.r1=Radiobutton(window, text="Confirmed Cases", variable=self.v0,value=1, command=self.confirmCases)
        self.r2=Radiobutton(window, text="Deaths", variable=self.v0,value=2, command=self.deaths)
        self.r3=Radiobutton(window, text="Recovered", variable=self.v0,value=3, command=self.recovered)
        self.r4=Radiobutton(window, text="Active Cases", variable=self.v0,value=4, command=self.active)
        self.r5=Radiobutton(window, text="Incident Rate", variable=self.v0,value=5, command=self.incident)
        self.r6=Radiobutton(window, text="Fatality Ratio", variable=self.v0,value=6, command=self.fatality)
        self.r1.place(x=30,y=70)
        self.r2.place(x=180, y=70)
        self.r3.place(x=270, y=70)
        self.r4.place(x=390, y=70)
        self.r5.place(x=510, y=70)
        self.r6.place(x=630, y=70)

        self.lbl=Label(window, text="Select the Order of Data", fg='Black', font=("Helvetica", 14))
        self.lbl.place(x=30, y=130)
        self.v=IntVar()
        self.v.set(1)
        self.r1=Radiobutton(window, text="Max to Min", variable=self.v,value=1, command=self.maxtomin)
        self.r2=Radiobutton(window, text="Min to Max", variable=self.v,value=2, command=self.mintomax)
        self.r1.place(x=30,y=170)
        self.r2.place(x=180, y=170)


        self.lbl=Label(window, text="Select the Range of Data", fg='Black', font=("Helvetica", 14))
        self.lbl.place(x=30, y=230)
        self.var = StringVar()
        self.var.set("All")
        self.data=("top 5", "top 15", "top 30")
        self.cb=Combobox(window, values=self.data)
        self.cb.bind("<<ComboboxSelected>>", self.combobox)
        self.cb.place(x=30, y=270)

    def confirmCases(self):
        self.index = 1

    def deaths(self):
        self.index = 2
    
    def recovered(self):    
        self.index = 3

    def active(self):        
        self.index = 4

    def incident(self):       
        self.index = 6

    def fatality(self):
        self.index = 7
    
    def maxtomin(self):
        self.max = True

    def mintomax(self): 
        self.max = False

    def proceed(self):
   
        cartesianTree = CartesianTree(covidDataNodes,self.index)
        sortedList = cartesianTree.priorityQueue(self.max, self.top)
        
        self.openNewWindow(self.window,sortedList)


    def combobox(self, x):
        self.top = self.cb.get()
        self.top = self.top[4:]
        self.top = int(self.top)

mywindow=Tk()
img1 = PhotoImage(file="maroonbg.png")
label = Label(mywindow, image=img1)
label.place(x=0, y=0)
img2 = PhotoImage(file="python-tkinter-background-image.png")
label = Label(mywindow, image=img2)
label.place(x=700, y=130)
mywin = Window(mywindow) 

mywindow.title('Covid Cases Worldwide')
mywindow.geometry("1000x400+240+160")

mywindow.mainloop()



