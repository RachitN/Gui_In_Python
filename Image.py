import tkinter
root = tkinter.Tk()
photo = tkinter.PhotoImage(file='bca1.png')
label1 = tkinter.Label(root,image=photo)
label1.pack()
root.mainloop()