import tkinter
import customtkinter
from pytube import YouTube

# This Progrm was gotten from a youtube video and will be futher improved upon

def startDownload():
    try:
        youtube = YouTube(url_path.get(), on_progress_callback=progress)
        youObj = youtube.streams.get_highest_resolution()
        label.configure(text=youObj.title)
        youObj.download()
        error.configure(text="Downloaded")
    except:
        error.configure(text="Download Error")


def progress(stream, chunk, bytes_remaining):
    file_size = stream.filesize
    bytes_downloaded = file_size - bytes_remaining
    percentage = bytes_downloaded / file_size * 100
    progress_label.configure(text=str(int(percentage)) + "%")
    progress_label.update()
    progress_bar.set(float(percentage)/100)
    progress_bar.update()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


app = customtkinter.CTk()
app.geometry("780x540")
app.title("Youtube Downloader")

url_path = tkinter.StringVar()

label = customtkinter.CTkLabel(app, text="YouTube Downloader App")
label.pack(padx=10, pady=10)

input_element = customtkinter.CTkEntry(app, width=400, textvariable=url_path)
input_element.pack(padx=20, pady=10)

error = customtkinter.CTkLabel(app, text="")
error.pack()

progress_label = customtkinter.CTkLabel(app, text="0%")
progress_label.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=200)
progress_bar.set(0)
progress_bar.pack(pady=20)

button_element = customtkinter.CTkButton(app, text="Download", command=startDownload)
button_element.pack()

app.mainloop()
