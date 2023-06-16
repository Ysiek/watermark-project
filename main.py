from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk, ImageFilter


class Photo:
    def __init__(self):
        self.download_btn = None
        self.img = None
        self.img_name = None

    def upload_file(self):
        f_types = [('JPG File', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)

        img_pil_object = Image.open(filename)
        self.img = img_pil_object.convert('RGBA')

        # CREATE WATERMARK
        python_watermark = Image.open('python-logo.png')
        watermark = python_watermark.convert('RGBA').resize((100, 100))
        self.img.alpha_composite(watermark)

        # SHOW IMAGE
        photo = ImageTk.PhotoImage(self.img)
        label = Label(f, image=photo)
        label.image = photo
        label.place(x=200, y=200, anchor=CENTER)

        # SHOW LABEL, INPUT AND BUTTON TO DOWNLOAD PHOTO
        img_name_label = Label(f, text="Set name", foreground='white', background='grey')
        img_name_label.place(x=200, y=430, anchor=CENTER)

        self.img_name = Entry(f)
        self.img_name.place(x=200, y=450, anchor=CENTER)

        self.download_btn = Button(f, text='Download your new photo', command=self.dowload_image)
        self.download_btn.place(x=200, y=475, anchor=CENTER)

    def dowload_image(self):
        img_var = self.img_name.get()

        if img_var.strip(' ') == '':
            self.img_name.delete(0, END)
            return print('please set your img name')

        # DOWNLOAD IMAGE
        self.img.save(f"C:/Users/micha/OneDrive/Pulpit/{img_var}.png")


window = Tk()
window.geometry("400x500")

photo_manager = Photo()

style = Style()
style.configure('BW.TLabel', foreground='white', background='grey', font=("Arial", 25))
style.configure('My.TFrame', background='grey')

f = Frame(window, width=400, height=500, style='My.TFrame')
f.grid(row=0, column=0, sticky="NW")
f.grid_propagate(0)
f.update()

header = Label(f, text="Watermarking Photo", style='BW.TLabel')
header.place(x=200, y=30, anchor=CENTER)

img_btn = Button(f, text='Choose your image', command=photo_manager.upload_file)
img_btn.place(x=200, y=400, anchor=CENTER)

window.mainloop()
