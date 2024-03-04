import tkinter as tk
from tkinter import filedialog # returns touple, if empty ()
import numpy as np
import os
import pandas as pd
from scipy.stats import linregress


def destroy():
    global rioot
    rioot.destroy()

def fprint(df):                             #"fprint" makes a linear regression between the first local minimum maximum
    ar=df["log"]
    max1=np.where(ar==ar.max())[0][0]
    max2=np.where(ar==ar[max1+10:].max())[0][0]
    min1=np.where(ar==ar[max1:max2].min())[0][0]
    q=df["Q"][min1:max2]
    lin=df["log"][min1:max2]
    fit=linregress(q,lin)
    A,B=fit[0],fit[1]
    Q=df["Q"][:max2]
    Lin=df["log"][:max2]
    linprog=np.array([A*i+B for i in Q])
    linpro=Lin/linprog
    fcu=np.concatenate((linpro,ar[max2:]/ar.max()))
    linprogv=np.array([A*i+B for i in q])
    linprov=lin/linprogv
    fcv=np.concatenate((ar[:min1]/ar.max(),linprov,ar[max2:]/ar.max()))
    df["reg"]=fcv
    warnung="Warnung: bei der Footprintkorrektur kam es zu Zwischenfällen. Es mussten einige Werte korrigiert werden. Die Oszillation ist jedoch zuverlässig "
    warning="Warning: the footprintkorrektur didn't worked properly. Some values had to be corrigated. The oszillation is reliable"
    warningtext=warnung+"\n\n"+warning

    if(any(df["reg"]<0)):
        global rioot
        rioot=tk.Tk()
        notice=tk.Button(rioot,text=warningtext, command=destroy)           # if the fitted graph becomes negative, the footprint does not work, so here is a warning note. 
        notice.pack()

        df["reg2"]=fcu
        df.loc[df["reg"]<0]["ref"]=None


    return df

          


def DataFrame():
    
    root = tk.Tk()
    files_str = filedialog.askopenfilename(initialdir=os.getcwd()+"/dql/", filetypes=(('dql files', '*.dql'),('all files', '*.*')))
    root.destroy()

    with open(files_str, 'rb') as f:
        contents = f.read()

    fobj = str(contents).split("\\r")
    x=False 
    eins=[]
    zwei=[]


    for i,line in enumerate( fobj[:-1]):                            # This loop takes the data out of the dql-data and made two lists
        if ( "]" in line):
            dddd=2
        if x:
            reihe=line.replace(" ","").replace("\\n","")[:-1].split(",")
            eins.append(reihe[0])
            zwei.append(reihe[1])
        if("[Data]" in line):
            x=True


    df=pd.DataFrame({eins[0]:np.array([float(i) for i in eins[1:]]),zwei[0]:np.array([float(i) for i in zwei[1:]])})

    logi=np.log10(np.array([i for i in df["Det1Disc1"].replace(0,1)]))
    df["log"]=logi
    df["log"]=df["Det1Disc1"]
    df["Q"]=np.sin(df["Angle"]*np.pi/180)*np.pi*2/1.53   
    df=fprint(df)   
    df3=df.loc[df["Q"]>=0]
    df2=df3.loc[df["Q"]>=0]
    
    return df2,files_str





