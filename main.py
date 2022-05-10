from time import sleep
from tkinter import *
from tkinter import ttk

# UTILS
from utils.chromedriver import chromedriver
from tests.sign_in import sign_in
from tests.new_device import new_device
from tests.delete_device import delete_device


def run():
    webdriver = chromedriver.ChromeDriver()
    webdriver.maximize()
    runningStatus.delete("1.0", END)
    # Sign In Case
    signInStatus = sign_in.SignInCase(webdriver.driver).run()
    if signInStatus == True:
        runningStatus.insert(INSERT, "Sign In Case =============================> PASSED\n")
    if signInStatus == False:
        runningStatus.insert(INSERT, "Sign In Case =============================> FAILED\n")
    # New Device Case
    newDeviceStatus = new_device.NewDeviceCase(webdriver.driver).run()
    if newDeviceStatus == True:
        runningStatus.insert(INSERT, "New Device Case ==========================> PASSED\n")
    if newDeviceStatus == False:
        runningStatus.insert(INSERT, "New Device Case ==========================> FAILED\n")
    # Delete Device Case
    deleteDeviceStatus = delete_device.DeleteDeviceCase(webdriver.driver).run()
    if deleteDeviceStatus == True:
        runningStatus.insert(INSERT, "Delete Device Case =======================> PASSED\n")
    if deleteDeviceStatus == False:
        runningStatus.insert(INSERT, "Delete Device Case =======================> FAILED\n")
    webdriver.quit()


def quit():
    root.quit()


# BEGIN
root = Tk()
root.iconbitmap("icon.ico")
root.title("KMI Automation Testing")
root.state("zoomed")
ttk.Button(root, text="RUN", command=run).place(x=24, y=24)
runningStatus = Text(root, height=10, width=50)
runningStatus.place(x=24, y=72)
ttk.Button(root, text="Quit", command=quit).place(x=24, y=264)
root.mainloop()
# END
