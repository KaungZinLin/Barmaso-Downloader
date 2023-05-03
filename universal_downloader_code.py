import tkinter
from tkinter import *
from tkinter import messagebox
import requests


# Functions
def download_file():
    try:
        url = url_input_field.get()
        filename = file_name_input_field.get()

        response = requests.get(url)
        if response.status_code == 200:
            messagebox.showinfo("Info", "Please wait while your file is being downloaded...")
            with open(filename, "wb") as f:
                f.write(response.content)

            messagebox.showinfo("Info", "Your file has been downloaded!")
        else:
            messagebox.showerror("Error!", f"Error downloading {url}: {response.status_code}")
    except:
        messagebox.showerror("Error!", "An unknown error has occured!")


def about_app():
    messagebox.showinfo("About", "Universal by Barmaso Downloader\n\nThis is the app from the 'Barmaso Downloader' Suite and used for downloading universal files. \n\nApp Version: v0.1 for macOS\n\nHuge Thanks for Using this App!")

# GUI Setup
window = Tk()
window.title("Universal Downloader")
window.resizable(False, False)
window.config(padx=50, pady=50)

# Labels
universal_downloader_label = Label(text="Universal Downloader", font=('Areal', 35))
universal_downloader_label.grid(row=0, column=0, sticky='w')
by_barmaso_label = Label(text="by Barmaso")
by_barmaso_label.grid(row=1, column=0, sticky='w')

url_entry_label = Label(text="\nEnter URL (link) to download: ")
# url_entry_label.grid(row=2, column=0, sticky='w')

file_name_entry_label = Label(text="Enter file name to save: ")
# file_name_entry_label.grid(row=3, column=0, sticky='w')

note_label = Label(text="\nYour downloads will be saved to the location where you've put the app.", font=('Areal', 15))
note_label.grid(row=4, column=0, sticky='w')

# Entries
url_input_field = tkinter.Entry(window, width=45)
url_input_field.grid(row=2, column=0, sticky='w')
url_input_field.insert(0, 'Enter video link (URL): ')

def clear_text(event):
    if url_input_field.get() == 'Enter video link (URL): ':
        url_input_field.delete(0, 'end')


url_input_field.bind('<FocusIn>', clear_text)

file_name_input_field = tkinter.Entry(window, width=45)
file_name_input_field.grid(row=3, column=0, sticky='w')
file_name_input_field.insert(0, 'Enter file name to save: ')


def clear_text_2(event):
    if file_name_input_field.get() == 'Enter file name to save: ':
        file_name_input_field.delete(0, 'end')


file_name_input_field.bind('<FocusIn>', clear_text_2)

# Buttons
download_button = tkinter.Button(text="Download", width=15, command=download_file)
download_button.grid(row=5, column=0, sticky='w')

about_button = Button(text="About", width=15, command=about_app)
# about_button.grid(row=6, column=0, sticky='w')

# GUI Loop
window.mainloop()
