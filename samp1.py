import csv
import tkinter as tk  # PEP 8 recommends against `import *`.

# Create and set the GUI for the passScreen of the Password Manager.
def displayss(name):
    passScreen = tk.Tk()
    passScreen.geometry("1200x1200")
    passScreen.resizable(width=False, height=False)
    passScreen.title("Password")

    # col_names = ("Type", "Username", "Password", "Name", "Specific", "Date Created",
    #              "Date Updated")
    # for i, col_name in enumerate(col_names, start=1):
    #     tk.Label(passScreen, text=col_name).grid(row=3, column=i, padx=40)
    a=8
    with open(name, "r", newline="") as passfile:
        reader = csv.reader(passfile)
        data = list(reader)


    entrieslist = []
    for i, row in enumerate(data, start=4):
        entrieslist.append(row[0])
        for col in range(1, a):
            tk.Label(passScreen, text=row[col]).grid(row=i, column=col)

    passScreen.mainloop()