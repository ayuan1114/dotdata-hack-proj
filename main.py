import tkinter
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO
from recipe_output import RecipeApp

retval = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]
ings = []

added = 0

root = Tk()


Label(root, text="Select available ingredients").grid(column=0, row=0)

Label(root, text="").grid(column=0, row=1)
Label(root, text="").grid(column=0, row=2)

Label(root, text="Protein:").grid(row=3, column=0, sticky=W)
Label(root, text="").grid(row=4, column=0)
retval[0] = StringVar()
Checkbutton(root, text="Chicken", variable=retval[0], offvalue="", onvalue="Chicken").grid(row=5, column=0, sticky=W)
retval[1] = StringVar()
Checkbutton(root, text="Beef", variable=retval[1], offvalue="", onvalue="Beef").grid(row=6, column=0, sticky=W)
retval[2] = StringVar()
Checkbutton(root, text="Pork", variable=retval[2], offvalue="", onvalue="Pork").grid(row=7, column=0, sticky=W)
retval[3] = StringVar()
Checkbutton(root, text="Lamb", variable=retval[3], offvalue="", onvalue="Lamb").grid(row=8, column=0, sticky=W)

Label(root, text="Canned Goods:").grid(column=1, row=3, sticky=W)
Label(root, text="").grid(column=1, row=4)

retval[4] = StringVar()
Checkbutton(root, text="Chicken stock or broth", variable=retval[4], offvalue="", onvalue="Chicken Stock").grid(row=5,
                                                                                                                column=1,
                                                                                                                sticky=W)
retval[5] = StringVar()
Checkbutton(root, text="Beef stock or broth", variable=retval[5], offvalue="", onvalue="Beef Stock").grid(row=6,
                                                                                                          column=1,
                                                                                                          sticky=W)
retval[6] = StringVar()
Checkbutton(root, text="Tomato sauce", variable=retval[6], offvalue="", onvalue="Tomato Sauce").grid(row=7, column=1,
                                                                                                     sticky=W)
retval[7] = StringVar()
Checkbutton(root, text="Canned beans", variable=retval[7], offvalue="", onvalue="Canned Beans").grid(row=8, column=1,
                                                                                                     sticky=W)

Label(root, text="Starches and Dry Goods:    ").grid(row=3, column=2, sticky=W)
Label(root, text="").grid(row=4, column=2)
retval[8] = StringVar()
Checkbutton(root, text="Pasta", variable=retval[8], offvalue="", onvalue="Pasta").grid(row=5, column=2, sticky=W)
retval[9] = StringVar()
Checkbutton(root, text="Rice", variable=retval[9], offvalue="", onvalue="Rice").grid(row=6, column=2, sticky=W)
retval[10] = StringVar()
Checkbutton(root, text="Lentils", variable=retval[10], offvalue="", onvalue="Lentils").grid(row=7, column=2, sticky=W)

Label(root, text="Roots and Vegetables:").grid(row=3, column=3, sticky=W)
Label(root, text="").grid(row=4, column=3)
retval[11] = StringVar()
Checkbutton(root, text="Potatoes", variable=retval[11], offvalue="", onvalue="Potatoes").grid(row=5, column=3, sticky=W)
retval[12] = StringVar()
Checkbutton(root, text="Garlic", variable=retval[12], offvalue="", onvalue="Garlic").grid(row=6, column=3, sticky=W)
retval[13] = StringVar()
Checkbutton(root, text="Onions", variable=retval[13], offvalue="", onvalue="Onions").grid(row=7, column=3, sticky=W)
retval[14] = StringVar()
Checkbutton(root, text="Broccoli", variable=retval[14], offvalue="", onvalue="Broccoli").grid(row=8, column=3, sticky=W)
retval[15] = StringVar()
Checkbutton(root, text="Cabbage", variable=retval[15], offvalue="", onvalue="Cabbage").grid(row=9, column=3, sticky=W)
retval[16] = StringVar()
Checkbutton(root, text="Spinach", variable=retval[16], offvalue="", onvalue="Spinich").grid(row=10, column=3, sticky=W)

misc = StringVar()
Label(root, text="Add additional ingredients:").grid(column=1, row=15 + added, sticky=E)
edit = Entry(root, textvariable=misc).grid(row=15, column=2)


def add():
    global added
    global ings
    ings.append(misc.get())
    Label(root, text=misc.get()).grid(column=2, row=(17 + added))
    misc.set("")
    added += 1


butt = Button(text='Add', command=add).grid(row=15, column=3, sticky=W)
Label(root, text="Added:").grid(column=2, row=16)


def submit():
    for i in range(len(retval)):
        if (not retval[i].get() == ""):
            ings.append(retval[i].get())
    for widget in root.winfo_children():
        widget.destroy()
    app = RecipeApp(root, ings)


submit = Button(text='Submit', command=submit).grid(row=15, column=4)


mainloop()
