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

entryPath = ''
basewidth = 1000

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def helloCallBack():
       global entryPath, entryfolder
       folder_selected = filedialog.askdirectory()
       print("I'm clicked")
       
       message = tk.Label(root, text=folder_selected)
       message.pack()
       print("folder_selected:" + folder_selected)
       entryPath = folder_selected[:folder_selected.rindex('/')]
       if folder_selected != '':
              traverse_dir_recur(folder_selected)
       else:
              print("no directory selected")
              
              
def traverse_dir_recur(dir):
       global entryPath, basewidth
       dirList = os.listdir(dir)
       # create result directory
       final_directory = os.path.expanduser('~') + '/Documents/tmp' + dir[len(entryPath):]
       if not os.path.exists(final_directory):
              os.makedirs(final_directory)
       for dirname in dirList:
              f = os.path.join(dir, dirname)
              if os.path.isdir(f):
                     print("current is directory:" + f)
                     traverse_dir_recur(dir + "/" + dirname +"/")
              # else:
                     # print(f)
              # checking if it is a file
              if os.path.isfile(f):
                     # check if file is an image
                     filetype = imghdr.what(f)
                     if (filetype is None or filetype == ''):
                            print(f + "is not an image file, skip it")
                            continue
                     img = Image.open(f)
                     if v1.get() > 1.0:
                            # use setted percentage if scale bar was setted under 100
                            basewidth = int(float(img.size[0]) * v1.get()/100.0)
                     
                     wpercent = (basewidth/float(img.size[0]))
                            
                     hsize = int((float(img.size[1])*float(wpercent)))
                     img = img.resize((basewidth, hsize), Image.LANCZOS)
                     img.save(final_directory + '/' + dirname)
                     print(f)
        

l3 = Label(root, text = "result percentage")
v1 = DoubleVar()
s1 = Scale( root, variable = v1,
		from_ = 1, to = 100,
		orient = HORIZONTAL)

button = tk.Button(root, text ="choose folder", command = helloCallBack)



s1.pack(anchor = CENTER)
# defalut value
s1.set(1) 
# l3.pack()
l3.pack()
# l.pack(pady=(10, 0)) 
button.pack(pady=(100, 0))

# keep the window displaying
root.mainloop()



