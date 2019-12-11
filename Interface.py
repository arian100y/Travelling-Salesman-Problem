import tkinter as tk
import matplotlib.pyplot as plt
from DynammicProgramming import *




window = tk.Tk()
window.geometry("600x600")
# Code to add widgets will go here...


xset1=[]
yset1=[]
for i in reco:
    x1=db[i[0]][0]
    y1 = db[i[0]][1]
    xset1 += [x1]
    yset1+= [y1]

xset1 += [xset1[0]]
yset1 += [yset1[0]]






set1B = tk.Button(window, text="SET 1", command=set1,width = 20).place(x=10,y=100)
set2B = tk.Button(window, text="SET 2", command=set1,width = 20).place(x=10,y=150)
set3B = tk.Button(window, text="SET 3", command=set1,width = 20).place(x=10,y=200)
w = tk.Label(window, text="Hello, world!")

window.mainloop()