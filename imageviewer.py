from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title("Image viewer")
root.iconbitmap('d:/python things/random_wq3_2.ico')

image1 = ImageTk.PhotoImage(Image.open("D:/python things/photos/IMG_4374.jpg"))
image2 = ImageTk.PhotoImage(Image.open("D:/python things/photos/IMG_4375.jpg"))
image3 = ImageTk.PhotoImage(Image.open("D:/python things/photos/IMG_4376.jpg"))
image4 = ImageTk.PhotoImage(Image.open("D:/python things/photos/IMG_4377.jpg"))


imglist = [image1, image2, image3, image4]


mylab = Label(image= image1)
mylab.grid(row=0, column=0, columnspan=3)


def forward(imgnum):
    global mylab
    global button_fwd
    global button_bck

    mylab.grid_forget()
    mylab = Label(image= imglist[imgnum - 1 ])

    button_bck = Button(root, text="<<", command=lambda: backward(imgnum -1))
    button_fwd = Button(root, text=">>", command=lambda: forward(imgnum +1))

    if imgnum == 4:
        button_fwd = Button(root, text=">>", state= DISABLED)

    

    button_bck.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)
    mylab.grid(row=0, column=0, columnspan=3)

    


def backward(imgnum):
    global mylab
    global button_fwd
    global button_bck

    mylab.grid_forget()
    mylab = Label(image= imglist[imgnum - 1])

    button_bck = Button(root, text="<<", command=lambda: backward(imgnum -1))
    button_fwd = Button(root, text=">>", command=lambda: forward(imgnum +1))

    button_bck.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)
    mylab.grid(row=0, column=0, columnspan=3)

button_bck = Button(root, text="<<", command=backward, state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_fwd = Button(root, text=">>", command=lambda:forward(2))


button_bck.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_fwd.grid(row=1, column=2)





root.mainloop()