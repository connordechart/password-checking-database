import requests
from databases import database
import tkinter
from tkinter import Button, messagebox
import os
import threading

count = 0

def one_time_validation():
    if not os.path.isfile(os.environ["TEMP"] + "/confirmation.txt"):
        validation = messagebox.askyesno(
            "Rules", "I agree to not steal the software and redistribute it on my name and I understand that the app does not store any information from the user.")
    else:
        validation = True

    if validation:
        open(os.environ["TEMP"] + "/confirmation.txt", 'w+')

    return validation


def check():
    def _check():
        global count
        req = requests.get(i)
        if entry.get() in req.text:
            tkinter.Label(text=f"PASSOWORD FOUND IN DATABASE {count}",fg="red").pack()
        else:
            tkinter.Label(text=f"DATABASE {count} CLEAN", fg="green").pack()
        count += 1
    global entry
    for i in database.databases:
        threading.Thread(target=_check).start()


def databases():
    tk = tkinter.Tk()
    label = tkinter.Label(tk, text=[i.lstrip("https://github.com/danielmiessler/SecLists/blob/master/Passwords/")
                                     .lstrip("https://github.com/danielmiessler/SecLists/raw/master/Passwords/")
                                     .rstrip("?raw=true")
                                    + "\n" for i in database.databases]).pack()

    tk.mainloop()


window = tkinter.Tk()
count = 0

if one_time_validation():
    tkinter.Label(text="Password").pack()
    entry = tkinter.Entry()
    entry.pack()
    button = tkinter.Button(text="Start", command=check).pack()
    button1 = tkinter.Button(text="Databases", command=databases).pack()
    tkinter.Label(text=f"current databases {len(database.databases)}").pack()
    window.mainloop()
else:
    messagebox.showerror(
        title="Error", message="You must agree to the rules if you want to use the app")
