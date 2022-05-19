
import tkinter as tk
from switch import *
from tkinter import messagebox
import threading
import os

window = tk.Tk()
window.columnconfigure([0, 1, 2], weight=0, minsize=100)
window.rowconfigure([0, 1, 2], weight=0, minsize=100)

def make_choice(c):

    global choice
    choice = c

    if choice == "1":
        btn2.configure(bg="black")
        btn1.configure(bg="green")

    else:
        btn1.configure(bg="black")
        btn2.configure(bg="green")


def execute():

    host = entry_ip.get()
    username = entry_username.get()
    password = entry_password.get()
    commands = [ "show mac address-table dynamic", "show IP arp", "show version"]

    try:
        if os.path.isfile("terminaloutput.csv"):
            os.remove("terminaloutput.csv")
        
        for command in commands: 

            if main(choice, host, username, password, command):
                window.update()

            else:
                messagebox.showwarning("Warning", "Enter Valid IP/username/password")
                return
        
        for i in window.grid_slaves():
            i.destroy()

        window.columnconfigure([0, 1, 2], weight=0, minsize=100)
        window.rowconfigure([0, 1, 2], weight=0, minsize=100)
        label_connected = tk.Label(text="Commands Executed!")
        label_connected.grid(row=1, column=1)
        return

    except NameError:
        messagebox.showwarning("Warning", "Choose a\nMethode To Connect")
  

def run():

    threading.Thread(target=execute).start()
        
        

btn1 = tk.Button(text="SSH", background="black", fg="white", command=lambda c="1": make_choice(c), width=10, height=2)
btn1.grid(row=0, column=0, sticky="ew")

btn2 = tk.Button(text="Telnet", background="black", fg="white", command=lambda c="2": make_choice(c), width=10, height=2)
btn2.grid(row=0, column=2, sticky="ew")


window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight=0, minsize=20)

label_ip = tk.Label(text="IP address")
entry_ip = tk.Entry(window)


label_username = tk.Label(text="Username")
entry_username = tk.Entry(window)


label_password = tk.Label(text="Password")
entry_password = tk.Entry(window, show="*")


label_ip.grid(row=2, column=1)
entry_ip.grid(row=3, column=1)

label_username.grid(row=4, column=1)
entry_username.grid(row=5, column=1)

label_password.grid(row=6, column=1)
entry_password.grid(row=7, column=1)



button_connect = tk.Button(window, text="Connect & Execute", background="black", fg="white", command=run, width=15, height=2)
button_connect.grid(row=8, column=1)


tk.mainloop()
