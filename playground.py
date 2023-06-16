from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk

def upload_file():
    global photo
    f_types = [('JPG File', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    #SHOW IMAGE
    label.config(image=photo)


window = Tk()



style = Style()
style.configure('BW.TLabel', foreground='white', background='grey', font=("Arial", 25))
style.configure('My.TFrame', background='grey')

label = Label()
label.pack()

img_btn = Button(text='Choose your image', command=upload_file)
img_btn.pack()


window.mainloop()