# Hello, if are you erudited in python, maybe you will disprize this script. My skills are rudimentary and I am happy it works. I'm not familiar with conventions. So many names can be silly.
# I named the StringVars like the Buttons, Lables or Entrys they belong. But the StringVar names have lower-case letters.
# feel free to change stupid parts.


import numpy as np
import matplotlib.pyplot as plt
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import xandy
import pandas as pd
import doku

class function:
    xlist=[]                            # the xlist is the list of x-coordinates of all marked points
    ylist=[]                            # the equal y-values
    border=0.2                          # the x-value until the graph will be painted
    x=np.linspace(0,20,100)
    y=np.sin(x)
    hoverpoint=(0,0)                    
    onoff={True:"On",False:"Off"}           # if the pointer is visible the boolean is true. "onoff" is for the description on the button. 

    def average(self):                                    # figure out the average and show it on the gui
        abstls=[]
        vv=sorted(self.xlist)                               # the function takes the list of the marked points....
        if (len(vv)>= 2):                   
            for i,v in enumerate(vv[:-1]):                               # ...and if the list ist larger than two, the average will be figured out.
                abstls.append(vv[i+1]-v)
            self.Thickness["text"]="thickness: ",2*np.pi/np.mean(np.array(abstls))
        else:
            self.Thickness["text"]="not engough points"                 

    def deletpoints(self):              # Delete points, 
        self.xlist=[]                   # it clears the xlist of the marked points...
        self.setylist()                 # ...the ylist too...
        self.paint()                    # ....and paint everything new.
        self.average()
       
    def hover(self,event):
        try:
            ix,iy=self.minimum(event.xdata,event.ydata)  # The closest point that the cursor will be figured out. 
        except:
            ix=0

        try:
            self.hoverpoint=(ix,iy)
        except:
            4
        self.paint()            # The green point will be painted in the paint function. This makes a lot of trouble, cause the whole stuff will be painted every time and everything is slower, but I didn't find another way so far. Maybe you can?


    def paint(self):                # This function will be used every time. Unfortunately, it is a little laborious.
        self.axes.cla()                                                                 # At first, everthing will be deleted. 
        self.axes.plot(self.x[self.x<=self.border],self.y[self.x<=self.border])         # The graph will be painted
        self.axes.set_ylabel("R",rotation=0,loc="top",fontsize = 15 )
       # self.axes.set_xlabel("q [\u212B⁻¹]",fontsize = 15 ,loc="right")               # (native xlabel. It is out of the canvas if you define it on this way.)

        self.axes.tick_params(axis="x",labelsize=15)
        self.axes.tick_params(axis="y",labelsize=15)

        try:
            self.axes.scatter(self.xlist,self.ylist,color="orange")                     # The marked points will be painted.
            if (self.withpointer.get()):
                self.axes.scatter(self.hoverpoint[0],self.hoverpoint[1],color="green")
        except:
            print("scatter failed")

        
        self.axes.set_yscale("log")

        if(self.hoverpoint[0] in self.xlist):                                           # If you hover over a marked point, the point changes to red. It's useful if you want to.
            self.axes.scatter(self.hoverpoint[0],self.hoverpoint[1],color="red")
        try:
            self.numericleftborder=float(self.NLB.get())   # left and right border are the spots from and until the graph will be painted. Per default is from the beginning until the value "border"
        except:
            self.numericleftborder=0.025

        try:
            self.numericrightborder =float(self.NRB.get())
        except:
            self.numericrightborder=self.border
        self.canvas.draw()

    def loading (self):
        df,name=xandy.DataFrame()                            # The dataset will be loaded and converted in DataFrame(). 
        self.Title["text"]=self.namemaker(name)
        self.x=df["Q"]
        self.y=df["reg"]
        self.root.title(self.title.get())

    def loaddata(self):
        self.loading()
        self.paint()

    def minimum(self,ix,iy):                            # "minimum" calculates the closest point on the graph to the hovered point and return the coordinates.
        difx=abs(self.x-ix)
        closest=np.where(difx==difx.min())[0][0]
        xmin=np.array(self.x)[closest]
        ymin=np.array(self.y)[closest]
        return xmin,ymin
       
    def namemaker(self, string):              # This function takes the name of the dql.data end erases the "dql.part". The name will be on the top of the gui.
        a=0
        for j,k in enumerate( [i=="/" for i in string]):
            if (k):
                a=j
        dql=string[a+1:]
        return dql[:-4] 


    def numeric(self):                      # The numeric-function consider every point and checks, if the point is a local maximum in a definable range around the point.
        self.deletpoints()
        
        if(self.numericleftborder>=0):                  # The border of this investigation are adjustable over the gui,...
            l=self.numericleftborder
        else:
            l=0.02                                      # ... per default it is from 0.02 ...
        if(self.numericrightborder<=self.border):
            r=self.numericrightborder
        else:
            r=self.border                                     # ... until the end of the graph

        y=self.y[[i<=r for i in self.x]]
       
        try:
            range=int(self.Numrange.get())
            
        except:
            range=1                                    # The default range is from 1 left to 1 right. 
        self.xlist=[]
        for i,v in enumerate(y):
            if(np.array(self.x)[i]>=l):
                if(i-range>=0 and i+range<len(y)):

                    if(v==y[i-range:i+range+1].max()):
                        self.xlist.append(np.array(self.x)[i])

        self.setylist()
        self.average()
        self.paint()

    def onclick(self,event):                         # "onklick" marks the closest point to the cursor.
        ix,iy=self.minimum(event.xdata,event.ydata)     # The closest point will be calculated over the minimum-function.
        if (ix in self.xlist):
            self.xlist.remove(ix)
        else:
            self.xlist.append(ix)                         # The point will be added or removed to the list of marked points, dependent if it's already on the list.
        
        self.setylist()
        self.paint()

        self.average()
                   
    def pointer_onoff(self):                                        # "pointer-onoff" changes the boolean if the pointer shall be on or off.
        self.withpointer.set(not self.withpointer.get())
        self.pointerboolean.configure(text=self.onoff[self.withpointer.get()])
        self.paint()

    def quit(self):                       # Destroys the root and end the script.
        self.root.destroy()

    def Reload(self):                                 # "Reload" paints the graph again. It is necessary if you changed the right border until the graph shall be painted.
        try:
            self.border=float(self.End_of_graph.get())
        except:
            self.border=0.2     
        self.paint()

    def savewindow(self):
        df=pd.DataFrame({"Q":self.x,"R":self.y})
        data = [('csv', '*.csv')]
        file_out = tkinter.filedialog.asksaveasfile(filetypes=data,initialfile = self.Title["text"])    # q-values and R-values will be stored in a csv.data.
        df_testFile.to_csv(file_out, index=False, encoding="utf-8")
  

    def setylist(self):                                                   #"setylist"  calculates the list of y-values of the marked points
        indexnumbers=[list(self.x).index(i)for i in self.xlist]
        self.ylist=[list(self.y)[i] for i in indexnumbers]




    def __init__(self,x=np.linspace(0,20,100),y=np.sin(x)):             # the "__init__-"function is sorted by the place where the buttons are in the gui
       
        self.x=np.array(x)
        self.y=np.array(y)
        self.root=tkinter.Tk()
        tkinter.Grid.columnconfigure(self.root, 0, weight=1)
        tkinter.Grid.rowconfigure(self.root, 1, weight=1)

        self.border=0.2                     # Per default, all graphs will be painted until q=0.2.
        self.numericleftborder=0.025
        self.numericrightborder=self.border

# --------------Frame0----------------

        self.Frame0=tkinter.Frame(self.root)
        self.Frame0.grid(sticky = "EW" , row = 0)

  
        tkinter.Grid.columnconfigure(self.Frame0, 1, weight=1)
        tkinter.Grid.columnconfigure(self.Frame0, 0, weight=1)


        self.title=tkinter.StringVar(self.Frame0) # --------------name of the graph
        self.Title=tkinter.Label(self.Frame0,textvariable=self.title.get() ,font = 30)
        self.Title.grid(column=0,row=0)
        self.Title.config(width=30)   



        datenbutton=tkinter.Button(self.Frame0, text = "load Data",command=self.loaddata ) #----------------load the dataset
        datenbutton.grid(column = 1 , row = 0 ,sticky = "E")

# --------------Frame0----------------



# --------------Frame1----------------
        self.Frame1=tkinter.Frame(self.root)
        self.Frame1.grid(sticky="EWNS",row =1 )
        tkinter.Grid.rowconfigure(self.Frame1, 0, weight = 1 )
        tkinter.Grid.columnconfigure(self.Frame1, 0, weight = 1 )


        self.Frame11=tkinter.Frame(self.Frame1)
        self.Frame11.grid(column=0,row=0,sticky="NSWE")


        self.Frame11.grid(sticky="EWNS",column=0,row=0 )
        tkinter.Grid.rowconfigure(self.Frame11, 0, weight = 1 )
        tkinter.Grid.columnconfigure(self.Frame11, 0, weight = 1 )


# --------------Frame1----------------





#----------------------------------------------------------Frame2/Framenum------------------------------------------------------------------
        self.Frame2=tkinter.Frame(self.root)
        self.Frame2.grid(sticky = "SEW",row = 2)   
        self.Framenum = tkinter.Frame(self.Frame2 ,  highlightbackground="blue", highlightthickness=1)
        self.Framenum.grid(column = 1)

        self.Frame2b=tkinter.Frame(self.Frame2)
        self.Frame2b.grid(column = 0,row = 0, sticky = "E")             

        tkinter.Grid.columnconfigure(self.Frame2, 2, weight=1)
        tkinter.Grid.columnconfigure(self.Frame2, 1, weight=1)

        self.withpointer=tkinter.BooleanVar() #-------------the green pointer
        self.withpointer.set(True)    
        self.pointerboolean=tkinter.Button(self.Frame2b,text=self.onoff[self.withpointer.get()],command=self.pointer_onoff)
        self.pointerboolean.grid()

        xdelete=tkinter.Button(self.Frame2b, text ="delete points",command=self.deletpoints) #---------------delete all marked points
        xdelete.grid()

        dokubutton=tkinter.Button(self.Frame2b, text="docu", background="blue", command=doku.interdoku)   # ---doku will be loaded
        dokubutton.grid()

# ------------------------------------Framenum -----------------------------------------

        numericbutton=tkinter.Button(self.Framenum, text="numerisch",command=self.numeric)
        numericbutton.grid(column = 1, row = 2)

        self.nrbl=tkinter.StringVar()
        self.nrbl.set("from")
        self.NRBl=tkinter.Label(self.Framenum,textvariable=self.nrbl, width=9)
        self.NRBl.grid(column = 0, row = 0 , sticky ="E")

        self.nlb=tkinter.StringVar()
        self.NLB=tkinter.Entry(self.Framenum,textvariable=self.nlb, width=9)
        self.NLB.grid(column = 1, row = 0)

        self.nrbl=tkinter.StringVar()
        self.nrbl.set("till")
        self.NRBl=tkinter.Label(self.Framenum,textvariable=self.nrbl, width=9)
        self.NRBl.grid(column = 0, row = 1,sticky ="E" )        
        self.nrb=tkinter.StringVar()
        self.NRB=tkinter.Entry(self.Framenum,textvariable=self.nrb, width=9)
        self.NRB.grid(column = 1, row = 1)
       
        self.numrange=tkinter.StringVar()
        self.Numrange=tkinter.Entry(self.Framenum,textvariable=self.numrange, text="6")
        self.Numrange.grid(column = 0, row = 2)
                
        numericbutton=tkinter.Button(self.Framenum, text="numerisch",command=self.numeric)
        numericbutton.grid(column = 1, row = 2)

# ------------------------------------Framenum -----------------------------------------
#----------------------------------------------------------Frame2/Framenum------------------------------------------------------------------






# --------------Frame3----------------

        self.Frame3=tkinter.Frame(self.Frame2)
        self.Frame3.grid(column=2, row = 0,sticky = "E")     
        tkinter.Grid.columnconfigure(self.Frame3, 0, weight=1)

        self.end_of_graph=tkinter.StringVar()      #-------------- until the graph is painted
        self.End_of_graph=tkinter.Entry(self.Frame3,textvariable=self.end_of_graph)
        self.End_of_graph.grid(sticky = "E")
        rangebutton=tkinter.Button(self.Frame3, text="Reload",command=self.Reload)
        rangebutton.grid(sticky = "E")

# --------------Frame3----------------



# --------------Frame4----------------

        self.Frame4=tkinter.Frame(self.Frame2)
        self.Frame4.grid(sticky = "SEw",row=1, columnspan = 3 )
        tkinter.Grid.columnconfigure(self.Frame4, 0, weight=1)
        self.save=tkinter.Button(self.Frame4, text="save as csv", command = self.savewindow)
        self.save.grid(column = 0, row = 0)        
        self.save=tkinter.Button(self.Frame4, text="Quit" ,command = self.quit)
        self.save.grid(column = 1, row = 0)   

        self.thickness=tkinter.StringVar(self.Frame4)                           #calculated thickness
        self.Thickness=tkinter.Label(self.Frame4,text=self.thickness.get(), font = 30)
        self.Thickness.config(width=20)        
        self.Thickness.grid(row = 1,columnspan = 3,sticky = "EW")



# --------------Frame4----------------

               

# ------------------------------generates the interactive graphic--------------------------------------
        self.loading()                          
        self.fig=plt.Figure()
        self.axes=self.fig.add_subplot(111)
        self.canvas=FigureCanvasTkAgg(self.fig,master=self.Frame11)
        self.canvas.draw()                   #xlabel is defined over canvas. Otherwise, the label wouldn't reach over the canvas
        self.q=tkinter.Label(self.Frame1, text= "q [\u212B⁻¹]" , background="white", font =" Helvetica 15 ")

        self.q.grid(row=0,column=0, sticky="SE")
        self.canvas.get_tk_widget().grid(sticky="nsew")

        connect_onclick = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        connect_onclick = self.fig.canvas.mpl_connect('motion_notify_event', self.hover)
# ------------------------------generates the interactive graphic--------------------------------------



        self.paint()
        self.root.mainloop()




function(np.linspace(0,20),np.linspace(0,40))

