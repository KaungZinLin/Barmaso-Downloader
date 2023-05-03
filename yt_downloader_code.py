import tkinter
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

# Functions
def download_in_mp4():
    try:
        url_data = url_input_field.get()  # move this line inside the function
        if url_data == "":
            messagebox.showerror("Error!", "Please put a URL (video link) in the textbox!")
            url_input_field.focus()
        else:
            yt = YouTube(url_data)
            stream = yt.streams.get_by_itag(22)
            messagebox.showinfo("Info", "Please wait while your video file is being downloaded...")
            stream.download()
            messagebox.showinfo("Info", "Your download was successful!")
    except:
        messagebox.showerror("Error!", "Cannot download your video file!")
        url_input_field.focus()



def download_in_mp3():
    try:
        url = url_input_field.get()
        yt = YouTube(url)

        if url_data == "":
            messagebox.showerror("Error!", "Please put a URL (video link) in the textbox!")
            url_input_field.focus()
        else:
            stream = yt.streams.get_audio_only()
            messagebox.showinfo("Info", "Please wait while your audio file is being downloaded...")
            stream.download()
            messagebox.showinfo("Info", "Your download was successful!")
    except:
        messagebox.showerror("Error!", "Cannot download your audio file!")
        url_input_field.focus()

def about_app():
    messagebox.showinfo("About", "YouTube Video Downloader by Barmaso Downloader\n\nThis is the app from the 'Barmaso Downloader' Suite and used for downloading YouTube Videos. \n\nApp Version: v0.1 for macOS\n\nHuge Thanks for Using this App!")

# GUI Setup
window = Tk()
window.title("YouTube Video Downloader")
window.resizable(False, False)
window.config(padx=50, pady=50)

window.columnconfigure(0, weight=0)

# Labels
yt_downloader_label = Label(window, text="YouTube Video Downloader", font=('Arial', 35))
yt_downloader_label.grid(row=0, column=0, sticky='w')

by_barmaso_label = Label(window, text="by Barmaso Downloader")
by_barmaso_label.grid(row=1, column=0, sticky='w')

note_label = Label(window, text="\nNOTE: Your downloads will be saved to the location where you've put the App.\n", font=('Arial', 15))
note_label.grid(row=3, column=0, sticky='w')

# Text Fields
url_input_field = tkinter.Entry(window, width=45)
url_input_field.grid(row=2, column=0, columnspan=2, sticky='w')
url_input_field.insert(0, 'Enter video link (URL): ')

url_data = url_input_field.get()

if url_data == "":
    messagebox.showerror("Error!", "Please put a URL (video link) in the textbox!")
    url_input_field.focus()

def clear_text(event):
    if url_input_field.get() == 'Enter video link (URL): ':
        url_input_field.delete(0, 'end')

url_input_field.bind('<FocusIn>', clear_text)

# Buttons
download_mp4_button = Button(text="Download in MP4", width=12, command=download_in_mp4)
download_mp4_button.grid(row=4, column=0, sticky='w')

download_mp3_button = Button(text="Download in MP3", width=12, command=download_in_mp3)
download_mp3_button.grid(row=5, column=0, sticky='w')

about_app_button = Button(text="About", width=12, command=about_app)
# about_app_button.grid(row=6, column=0, sticky='w')

# GUI Loop
window.mainloop()
