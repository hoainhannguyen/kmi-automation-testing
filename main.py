from tkinter import *
from tkinter import ttk

from tests.hello import hello
from tests.sign_in import sign_in


root = Tk()
root.title("KMI Automation Testing")
root.state('zoomed')
frm = ttk.Frame(root, padding=24)
frm.grid()
ttk.Button(frm, text="Hello Case", command=hello.run).grid(column=0, row=0)
ttk.Button(frm, text="Sign In Case", command=sign_in.run).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.quit).grid(column=0, row=2)
root.mainloop()
