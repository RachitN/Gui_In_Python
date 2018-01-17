import tkinter
root = tkinter.Tk()
topFrame = tkinter.Frame(root)
topFrame.pack()
bottomFrame = tkinter.Frame(root)
bottomFrame.pack(side="bottom")
buuton1 = tkinter.Button(topFrame,text="Button 1",fg="red")  #fg=`textcolor
buuton2 = tkinter.Button(topFrame,text="Button 2",fg="red")
buuton3 = tkinter.Button(topFrame,text="Button 3",fg="red")
buuton4 = tkinter.Button(bottomFrame,text="Button 4",fg="blue")
buuton1.pack(side="left")
buuton2.pack(side="left")
buuton3.pack(side="left")
buuton4.pack(side="bottom")

root.mainloop()