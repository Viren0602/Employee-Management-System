from tkinter import *
from PIL import ImageTk,Image

root = Tk()

f = Frame(root,width=1600,height=850,bg="red")
f.pack()

profile_pic = ImageTk.PhotoImage(Image.open("ems1.jpg"))
c = Canvas(f,width=1000,height=800)
c.create_image(0,0,anchor=CENTER,image=profile_pic)
c.place(x=50,y=50)
c.create_text(50,50,text="Hello World",font=("Monotype corsiva" , 40))
#l=Label(f,text="label")
#l.place(x=100,y=100)
root.mainloop()