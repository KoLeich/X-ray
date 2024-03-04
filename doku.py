#from turtle import window_height
import numpy as np
import matplotlib.pyplot as plt
import  tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)#,                                              NavigationToolbar2Tk)
#import xandy
#import pandas as pd
#import os

class interdoku:
   # xlist=[]
   # ylist=[]
   # border=0.2

    #hoverpoint=(0,0)
    anaus={True:"On",False:"Off"}



    def bind(self):
        a=2
        self.anzeige.set("")

    def Quit (self ):
        self.root.destroy()

    def draw_expl (self, a):
        self.anzeige.set(a)


    def pointer_onoff(self):
        self.withpointer.set(not self.withpointer.get())
        #print(self.withpointer.get())
        self.pointerboolean.configure(text=self.anaus[self.withpointer.get()])
        #self.paint()
        self.bind()


    def __init__(self):

        self.root=tkinter.Tk()
        self.root.geometry("600x400")
        self.root.configure(background='black')        
        pause = "\n\n________________\n\n\n"
        #numanger= "numerische Analyse: \n Alle Nachbarn eines jeden Punktes in einem Bereich werden werden betrachtet. Wenn sie alle einen geringeren R-Wert haben als der Punkt, wird der Punkt markiert.\n"
        #numaneng = "numeric analysis: \n all neigbours of every point in a scope  will be considered. If all of them have a lower R-value, the Point will be marked.\n"

        

        self.dokuger= { "load Data" : "Lade einen neuen Datensatz. ",
        "rightboarder" : "Stellt die rechte Grenze ein (default = 0.2) bis wo der Graph gezeichnet wird. \n Druecke anschlieszend auf \"Reload\"!",
        "reload" : "Zeichnet den Graph neu (bis zur neuen rechten Grenze). ",
        "delete points" : "Entfernt alle markierten Punkte.",
        "on/off" : "Der gruene Punkt wird an/aus gestellt. ",
        "numeric": "numerische Analyse: \n Alle Nachbarn eines jeden Punktes in einem Bereich werden werden betrachtet. \n Wenn sie alle einen geringeren R-Wert haben als der Punkt, wird der Punkt markiert.\n",
        "from" : " numerische Analyse: \n linke Grenze des Bereichts",
        "till" : " numerische Analyse: \n rechte Grenze des Bereichts",
        "[]" : "numerische Analyse: \n Anzahl der betrachteten Nachbarn auf jeder Seite",
        "numbutton" : "numerische Analyse: \n Numerisch berechnung wird durchgefuehrt \n alte punkte geloescht",
        "save as csv": "Speichert die Datentabelle.",
        "thickness" : "berechnete Schichtdicke ",
        "canvas": "interaktiver Visualisierung des Datensatzes"}


        self.dokueng = { "load Data" : " Load new data set.",
        "rightboarder" : "Adjust the right border until the graph is painted (default = 0.2). \nAfterward choose \"Reload\"! ",
         "reload" :"Graph will be painted againt (until the new right border).",
         "delete points" : "Delete all choosen points.", 
         "on/off" : "The green point will be turned on/off. ",
         "numeric":  "numeric analysis: \n all neigbours of every point in a scope  will be considered. \n If all of them have a lower R-value, the Point will be marked.\n",
         "from" : " numeric analysis: \n left border of the scope",
         "till" : "numeric analysis: \n right border of the scope",
         "[]" : "numeric analysis: \n number of choosen neigbours ",
         "numbutton" : "numeric analysis: \n Start numeric calculation \n old points will be destroyed.",
         "save as csv":"Save the data table.", 
         "thickness" :  "calculated thickness",
          "canvas": "interaktiv visualisation of the datatable"}

        self.pause = "\n\n________________\n\n"
        self.doku={}

        for key in self.dokueng.keys():
                self.doku[key]= self.dokuger[key]+pause+self.dokueng[key]



        tkinter.Grid.columnconfigure(self.root, 0, weight=1)
        tkinter.Grid.rowconfigure(self.root, 1, weight=1)



# --------------Frame0----------------

        self.Frame0=tkinter.Frame(self.root)#, background="red")
        self.Frame0.grid(sticky = "EW" , row = 0)

     #   self.Frame0a=tkinter.Frame(self.Frame0)#, background="red")
     #   self.Frame0a.grid(column = 0,row = 0)#, sticky = "W")
     #   self.Frame0b=tkinter.Frame(self.Frame0)#, background="red")
     #   self.Frame0b.grid(column = 1,row = 0, sticky = "W")   
        tkinter.Grid.columnconfigure(self.Frame0, 1, weight=1)
        tkinter.Grid.columnconfigure(self.Frame0, 0, weight=1)

# --------------Frame0----------------

        self.title=tkinter.StringVar()
        self.title.set("name of dql-Data ")
        self.Title=tkinter.Label(self.Frame0,textvariable=self.title ,font = 30)# , fontsize =50 )
       # self.Title=tkinter.Label(self.Frame0,text="self.title.get()" ,font = 30)# , fontsize =50 )
        self.Title.grid(column=0,row=0)
        self.Title.config(width=30) 

# --------------Frame1----------------

        self.Frame1=tkinter.Frame(self.root, background="white")

        self.Frame1.bind("<Enter>", lambda a="test", txt=self.doku["canvas"]: self.draw_expl(txt))

        self.Frame1.grid(sticky="EWNS",row =1 )

        tkinter.Grid.rowconfigure(self.Frame1, 0, weight = 1 )
        tkinter.Grid.columnconfigure(self.Frame1, 0, weight = 1 )


# --------------Frame1----------------








# --------------Frame2----------------

        self.Frame2=tkinter.Frame(self.root )#, background="green")
        self.Frame2.grid(sticky = "SEW",row = 2)   

        self.Framenum = tkinter.Frame(self.Frame2 ,  highlightbackground="blue", highlightthickness=1)#, background = "purple")
        self.Framenum.bind("<Enter>", lambda a="test", txt=self.doku["numeric"]: self.draw_expl(txt))

        

        self.Framenum.grid(column = 1)

        self.Frame2b=tkinter.Frame(self.Frame2)#, background="red")
        self.Frame2b.grid(column = 0,row = 0, sticky = "E")     

        tkinter.Grid.columnconfigure(self.Frame2, 2, weight=1)
        tkinter.Grid.columnconfigure(self.Frame2, 1, weight=1)

# --------------Frame2----------------

# --------------Frame3----------------

        self.Frame3=tkinter.Frame(self.Frame2 )#, background="blue")
        self.Frame3.grid(column=2, row = 0,sticky = "E")     
        tkinter.Grid.columnconfigure(self.Frame3, 0, weight=1)

# --------------Frame3----------------



# --------------Frame4----------------

        self.Frame4=tkinter.Frame(self.Frame2)#, background="brown")
        self.Frame4.grid(sticky = "SEw",row=1, columnspan = 3 )
        tkinter.Grid.columnconfigure(self.Frame4, 0, weight=1)



        self.save=tkinter.Button(self.Frame4, text="save as csv", command = self.bind)
        self.save.bind("<Enter>", lambda a="test", txt=self.doku["save as csv"]: self.draw_expl(txt))

        self.save.grid(column = 0, row = 0)
        
        self.save=tkinter.Button(self.Frame4, text="Quit" ,command = self.Quit, background="red")
        self.save.grid(column = 1, row = 0)        
# --------------Frame4----------------


        numericbutton=tkinter.Button(self.Framenum, text="numerisch",command = self.bind)
        numericbutton.grid(column = 1, row = 2)




        self.title=tkinter.StringVar(self.Frame0)
        self.Title=tkinter.Label(self.Frame0,text=self.title.get() ,font = 30)# , fontsize =50 )
        self.Title.grid(column=0,row=0)#, sticky="W")
        self.Title.config(width=30)        


        self.withpointer=tkinter.BooleanVar()
     #   self.withpointer.set(False)
        self.withpointer.set(True)       

     

        #self.loading()

        self.border=0.2
        self.numericleftborder=0.025
        self.numericrightborder=self.border
        self.entry1=tkinter.StringVar()
        self.textentry=tkinter.Entry(self.Frame3,textvariable=self.entry1)
        self.textentry.bind("<Enter>", lambda a="test", txt=self.doku["rightboarder"]: self.draw_expl(txt))        
        self.textentry.grid(sticky = "E")
        rangebutton=tkinter.Button(self.Frame3, text="Reload",command = self.bind)
        rangebutton.bind("<Enter>", lambda a="test", txt=self.doku["reload"]: self.draw_expl(txt))

        rangebutton.grid(sticky = "E")
        #self.fig=plt.Figure()
     #   self.axes=self.fig.add_subplot(111)
       # plt.yscale("log")

     #   self.canvas=FigureCanvasTkAgg(self.fig,master=self.Frame1)
     #   self.canvas=tkinter.Canvas(self.Frame1, width=200, height=100)

        self.anzeige=tkinter.StringVar(self.Frame1)
        self.anzeige.set("beschreibung \n just my \n immagination")
        self.Anzeige=tkinter.Label(self.Frame1, textvariable=self.anzeige, background="white")
        self.Anzeige["text"]="pimmel"
        self.Anzeige.grid()




        self.nrbl=tkinter.StringVar()
        self.nrbl.set("from")
        self.NRBl=tkinter.Label(self.Framenum,textvariable=self.nrbl, width=9)
        self.NRBl.bind("<Enter>", lambda a="test", txt=self.doku["from"]: self.draw_expl(txt))
        self.NRBl.bind("<Leave>", lambda a="test", txt=self.doku["numeric"]: self.draw_expl(txt))

        self.NRBl.grid(column = 0, row = 0 , sticky ="E")#(side="right")


        self.nlb=tkinter.StringVar()
        self.NLB=tkinter.Entry(self.Framenum,textvariable=self.nlb, width=9)
        self.NLB.bind("<Enter>", lambda a="test", txt=self.doku["from"]: self.draw_expl(txt)) 
        self.NLB.bind("<Leave>", lambda a="test", txt=self.doku["numeric"]: self.draw_expl(txt))

        self.NLB.grid(column = 1, row = 0)


        self.nrbl=tkinter.StringVar()
        self.nrbl.set("till")
        self.NRBl=tkinter.Label(self.Framenum,textvariable=self.nrbl, width=9)
        self.NRBl.bind("<Enter>", lambda a="test", txt=self.doku["till"]: self.draw_expl(txt))
        self.NRBl.bind("<Leave>", lambda a="test", txt=self.doku["numeric"]: self.draw_expl(txt))


        self.NRBl.grid(column = 0, row = 1,sticky ="E" )#(side="right")        
        self.nrb=tkinter.StringVar()
        self.NRB=tkinter.Entry(self.Framenum,textvariable=self.nrb, width=9)
        self.NRB.bind("<Enter>", lambda a="test", txt=self.doku["till"]: self.draw_expl(txt))
        self.NRB.bind("<Leave>", lambda a="test", txt=self.doku["numeric"]: self.draw_expl(txt))


        self.NRB.grid(column = 1, row = 1)#(side="right")
#------------------------------------------------------





        xdelete=tkinter.Button(self.Frame2b, text ="delete points",command = self.bind)
        xdelete.bind("<Enter>", lambda a="test", txt=self.doku["delete points"]: self.draw_expl(txt))
        xdelete.grid()
        
        self.handy=tkinter.StringVar(self.Frame4)
        self.handy.set(self.dokuger["thickness"]+"  -  "+self.dokueng["thickness"] )
        self.Handy=tkinter.Label(self.Frame4,text=self.handy.get(), font = 30)#,  fontsize =50 )
        self.Handy.config(width=20)        
        self.Handy.grid(row = 1,columnspan = 3,sticky = "EW")


        datenbutton=tkinter.Button(self.Frame0, text = "load Data",command = self.bind)
        datenbutton.grid(column = 1 , row = 0 ,sticky = "E")
        datenbutton.bind("<Enter>", lambda a="test", txt=self.doku["load Data"]: self.draw_expl(txt))

       
        self.entry2=tkinter.StringVar()
        self.numrange=tkinter.Entry(self.Framenum,textvariable=self.entry2,text="6")
        self.numrange.bind("<Enter>", lambda a="test", txt=self.doku["[]"]: self.draw_expl(txt))
        self.numrange.bind("<Leave>", lambda a="test", txt=self.doku["numeric"]: self.draw_expl(txt))

        self.numrange.grid(column = 0, row = 2)
        
        numericbutton=tkinter.Button(self.Framenum, text="numerisch",command = self.bind)
        numericbutton.bind("<Enter>", lambda a="test", txt=self.doku["numbutton"]: self.draw_expl(txt))
        numericbutton.bind("<Leave>", lambda a="test", txt=self.doku["numeric"]: self.draw_expl(txt))

        numericbutton.grid(column = 1, row = 2)


        self.pointerboolean=tkinter.Button(self.Frame2b,text=self.anaus[self.withpointer.get()],command = self.pointer_onoff)
        self.pointerboolean.bind("<Enter>", lambda a="test", txt=self.doku["on/off"]: self.draw_expl(txt))

        self.pointerboolean.grid()
        


        self.root.mainloop()
        self.ylist=[]
        self.xlist=[]



#interdoku()

