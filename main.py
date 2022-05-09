from tkinter import *
from tkinter import ttk

# UTILS
from utils.chromedriver import chromedriver
from tests.sign_in import sign_in

# WEBDRIVERS
webdriver = chromedriver.ChromeDriver()


def quit():
    webdriver.quit()
    root.quit()


# BEGIN
root = Tk()
root.iconbitmap("icon.ico")
root.title("KMI Automation Testing")
root.state("zoomed")
frm = ttk.Frame(root, padding=24)
frm.grid()
ttk.Button(frm, text="Sign In Case", command=sign_in.SignInCase(webdriver.driver).run).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=quit).grid(column=0, row=10)
root.mainloop()
# END
