import tkinter

root =tkinter.Tk()
name=tkinter.Label(root,text="Name")
age=tkinter.Label(root,text="Age")
Entry1=tkinter.Entry(root)
Entry2=tkinter.Entry(root)


def retrieve():
    input1=Entry1.get()
    input2=Entry2.get()
    input1=int(input1)+int(input2)
    print(input1)


but=tkinter.Button(root,text="Submit",command=retrieve)
name.grid(row=0)
age.grid(row=1)
Entry1.grid(row=0,column=1)
Entry2.grid(row=1,column=1)
but.grid(row=2)
root.mainloop()

