# Imports
from tkinter import *
from tkinter import messagebox
import subprocess

# Functions
def open_universal_downloader():
    try:
        subprocess.call(["open", "/Applications/Universal Downloader.app"])
    except:
        messagebox.showerror("Error!", "Cannot find Universal Downloader!\nMake sure to move the app to the Applications folder!")

def open_yt_video_downloader():
    try:
        subprocess.call(["open", "/Applications/YouTube Video Downloader.app"])
    except:
        messagebox.showerror("Error!", "Cannot find Universal Downloader!\nMake sure to move the app to the Applications folder!")

# GUI Setup
window = Tk()
window.title("Barmaso Downloader")
window.resizable(False, False)
window.config(padx=25, pady=25)

# Labels
barmaso_label = Label(text="Barmaso Downloader", font=('Areal', 25))
barmaso_label.grid(row=0, column=0, sticky='w')

download_option_label = Label(text="\nDOWNLOAD OPTIONS")
download_option_label.grid(row=1, column=0, sticky='w')

# Buttons
universal_button = Button(text="Universal Downloader", width=20, command=open_universal_downloader)
universal_button.grid(row=2, column=0, sticky='w')

yt_button = Button(text="YouTube Video Downloader", width=20, command=open_yt_video_downloader)
yt_button.grid(row=3, column=0, sticky='w')

# GUI Loop
window.mainloop()