import requests
import os
import tkinter as tk
from tkinter import messagebox
from subprocess import Popen

def download_file(url, destination_folder="."):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.join(destination_folder, url.split("/")[-1])
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Download successful: {filename}")
        else:
            print(f"Error downloading {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def start_download():
    urls  =     [     
    "https://github.com/SchBenedikt/Text-Editor/releases/download/v2024.01.04/text-editor.exe",
    "https://github.com/SchBenedikt/Text-Editor/blob/main/bold.png",
    "https://github.com/SchBenedikt/Text-Editor/blob/main/italic.png",
  "https://github.com/SchBenedikt/Text-Editor/blob/main/change_color.png",
  "https://github.com/SchBenedikt/Text-Editor/blob/main/change_bg_color.png",
  "https://github.com/SchBenedikt/Text-Editor/blob/main/decrease_font.png",
  "https://github.com/SchBenedikt/Text-Editor/blob/main/increase_font.png",
  "https://github.com/SchBenedikt/Text-Editor/blob/main/underline.png"

    ]
    download_folder = "Text-Editor"
    os.makedirs(download_folder, exist_ok=True)
    success = True

    for url in urls:
        download_file(url, download_folder)
        if not os.path.exists(os.path.join(download_folder, url.split("/")[-1])):
            success = False

    if success:
        messagebox.showinfo("Success", "All files were downloaded successfully.")
        open_folder_button.pack()  # Anzeigen des "Open Folder" Buttons nach erfolgreicher Installation
    else:
        messagebox.showerror("Error", "Some files failed to download. Please check the error messages above.")

def open_folder():
    download_folder = "Text-Editor"
    Popen(['explorer', download_folder])  # Öffnet den Ordner im Explorer

# GUI
root = tk.Tk()
root.title("Text-Editor Installation")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Click the button below to start the installation:")
label.pack(pady=10)

button = tk.Button(frame, text="Start Installation", command=start_download)
button.pack(pady=10)

open_folder_button = tk.Button(frame, text="Open Folder", command=open_folder)
# Der "Open Folder" Button wird zunächst nicht angezeigt und erscheint erst nach erfolgreicher Installation
open_folder_button.pack_forget()

root.mainloop()
