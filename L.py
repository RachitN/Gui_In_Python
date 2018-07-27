import tkinter
from tkinter import messagebox

root = tkinter.Tk()


def make_string(s):
    t = ""
    i = 0
    while s:
        a = s.count(s[i])
        t = t + str(a)
        s = s.replace(s[i], '')
    return t


def calculate(z):
    if len(z) == 2:
        z = z + '%'
        return z
    d = list(z)
    last = len(d) - 1
    first = 0
    z = ""
    if len(d) % 2 == 0:
        while first <= int((len(d) - 1) / 2):
            suM = int(d[first]) + int(d[last])
            first = first + 1
            last = last - 1
            z = z + str(suM)
    else:
        while first != int((len(d) - 1) / 2):
            suM = int(d[first]) + int(d[last])
            first = first + 1
            last = last - 1
            z = z + str(suM)
        z = z + (d[int((len(d)) / 2)])
    return calculate(z)


def retrieve():
    N1 = Entry1.get()
    N2 = Entry2.get()
    string = N1.upper() + "LOVES" + N2.upper()
    ns = make_string(string)
    z = calculate(ns)
    messagebox.showinfo("Result", z)


name = tkinter.Label(root, text="YOUR NAME")
age = tkinter.Label(root, text="PARTNER NAME")
Entry1 = tkinter.Entry(root)
Entry2 = tkinter.Entry(root)
but = tkinter.Button(root, text="Submit", command=retrieve)
name.grid(row=0)
age.grid(row=1)
Entry1.grid(row=0, column=1)
Entry2.grid(row=1, column=1)
but.grid(row=2)
root.mainloop()
