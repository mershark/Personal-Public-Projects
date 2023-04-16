'''
Author = Mershark Takyi
Lets connect = https://www.linkedin.com/in/mershark/
'''
import tkinter
import customtkinter
from pytube import YouTube

# function that downloads the youtube link when you click on the botton
def downloading():
    try:
        youtubelink = urlf.get()
        youtubecontent = YouTube(youtubelink)
        videotodownload = youtubecontent.streams.get_highest_resolution()
        videotodownload.download()
    except:
    # "sucmessage" can be found at the buttom of this codes
        sucmessage.configure(text="Download Error Check The Link")
    sucmessage.configure(text="Your Download Is Complete")

# This is the setting of the app
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# This is how the frame of the app will look like
app = customtkinter.CTk()
app.geometry("700x500")
app.title("A Youtube Downloader App")

# This works on the user interface
    # label
title = customtkinter.CTkLabel(app, text="Paste the link below")
title.pack(padx=12, pady=12)

    # input field
urlf = tkinter.StringVar()
inputfield = customtkinter.CTkEntry(app, width=300, height=50, textvariable=urlf)
inputfield.pack()

    # button
button = customtkinter.CTkButton(app, text="Download Now", command=downloading)
button.pack(padx=12, pady=12)

# message to display if download was succesful
sucmessage = customtkinter.CTkLabel(app, text="")
sucmessage.pack()


# You need this to be able to run the app
app.mainloop()