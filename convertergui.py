import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
from PIL import Image
import imghdr

root = tk.Tk()
root.title('image conveter')
window_width = 800
window_height = 400

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
# folder_selected = filedialog.askdirectory()
# print(folder_selected)

# # place a label on the root window
# message = tk.Label(root, text=folder_selected)
# message.pack()


def helloCallBack():
       folder_selected = filedialog.askdirectory()
       print("I'm clicked")
       
       message = tk.Label(root, text=folder_selected)
       message.pack()
       # make dir
       current_directory = os.getcwd()
       # final_directory = os.path.join(current_directory, r'result')
       # if not os.path.exists(final_directory):
       #        os.makedirs(final_directory)
       
       basewidth = 500

       # iterate over files in
       # that directory
       print("folder_selected:" + folder_selected)
       if folder_selected != '':
              # create result directory
              final_directory = os.path.join(folder_selected, r'result')
              if not os.path.exists(final_directory):
                     os.makedirs(final_directory)
              for filename in os.listdir(folder_selected):
                     
                     f = os.path.join(folder_selected, filename)
                     # checking if it is a file
                     if os.path.isfile(f):
                            # check if file is an image
                            filetype = imghdr.what(f)
                            if (filetype is None or filetype == ''):
                                   print(f + "is not an image file, skip it")
                                   continue
                            img = Image.open(f)
                            wpercent = (basewidth/float(img.size[0]))
                            hsize = int((float(img.size[1])*float(wpercent)))
                            img = img.resize((basewidth, hsize), Image.LANCZOS)
                            img.save(final_directory + '/' + filename)
                            print(f)
       else:
              print("no directory selected")

l3 = Label(root, text = "result percentage")
v1 = DoubleVar()
s1 = Scale( root, variable = v1,
		from_ = 1, to = 100,
		orient = HORIZONTAL)

button = tk.Button(root, text ="choose folder", command = helloCallBack)



s1.pack(anchor = CENTER)
# l3.pack()
l3.pack()
# l.pack(pady=(10, 0)) 
button.pack(pady=(100, 0))

# keep the window displaying
root.mainloop()



