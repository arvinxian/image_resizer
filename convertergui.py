import tkinter as tk
from tkinter import filedialog
from tkinter import *

root = tk.Tk()
root.title('image conveter')
window_width = 1280
window_height = 720

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# root.attributes('-alpha', 0.9)



# root.withdraw()
folder_selected = filedialog.askdirectory()
print(folder_selected)

# place a label on the root window
message = tk.Label(root, text=folder_selected)
message.pack()


def helloCallBack():
       print("I'm clicked")

button = tk.Button(root, text ="choose folder", command = helloCallBack)

button.pack()

# keep the window displaying
root.mainloop()