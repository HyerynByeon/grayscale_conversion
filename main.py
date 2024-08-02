import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import cv2
import numpy as np
from PIL import Image

root=Tk()
root.title("grayscale-conversion")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False,False)

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',filetype=(('JPF file','*.jpg'),
                                                                            ('PNG file','*.png'),
                                                                            ("ALL file",'*.txt')))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=310,height=270)
    lbl.image=img

def showGrayImage():
    global filename
    if hasattr(lbl, 'image'):
        # Read the image using OpenCV
        color_image = cv2.imread(filename)
        print(filename)
        print(color_image)

        # Convert the color image to grayscale
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

        # Convert the grayscale image to a PIL image and then to ImageTk
        gray_pil_image = Image.fromarray(gray_image)
        gray_image_tk = ImageTk.PhotoImage(gray_pil_image)

        # Display the grayscale image in the result image label
        lbl_result_image.configure(image=gray_image_tk, width=310, height=270)
        lbl_result_image.image = gray_image_tk


#frame
frame=Frame(root, width=710,height=370,bg="#fff")
frame.place(x=50,y=50)


#select image
selectimage=Frame(frame,width=340,height=350,bg="#d6dee5")
selectimage.place(x=10,y=10)

f=Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

label = tk.Label(f, text="Select the image", fg="white", bg="black", font=("Arial", 16))
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

lbl=Label(f,bg="black")
lbl.place(x=0,y=0)

Button(selectimage,text="Select Image",width=12,height=1,font="arial 14 bold",command=showimage).place(x=10,y=300)
Button(selectimage,text="Convert Image",width=12,height=1,font="arial 14 bold",command=showGrayImage).place(x=176,y=300)

#result image
result_image_frame = Frame(frame, width=340, height=350, bg="#c6ddef")
result_image_frame.place(x=360, y=10)

frame2 = Frame(result_image_frame, bd=3, bg="black", width=320, height=330, relief=GROOVE)
frame2.place(x=10, y=10)

placeholder_label = tk.Label(frame2, text="Result Image", fg="white", bg="black", font=("Arial", 16))
placeholder_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

lbl_result_image = Label(frame2, bg="black")
lbl_result_image.place(x=0, y=0)

root.mainloop()