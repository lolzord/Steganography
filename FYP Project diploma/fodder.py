from tkinter import *
from tkinter import messagebox
import ast
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb #stegano

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password==r[username]:  #read database here
        stg=Toplevel(root)
        stg.title("Image Steganography System - MSU")
        stg.geometry("700x500+250+180")
        stg.resizable(False,False)
        stg.configure(bg="#008080")

        def showimage():
            global filename
            filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetype=(("PNG File","*.png"), ("JPG File","*.jpg"), ("All File", "*.txt")))
            img=Image.open(filename)
            img=ImageTk.PhotoImage(img)
            lbl.configure(image=img,width=250,height=250)
            lbl.image=img

        def Hide():
            global secret
            message=text1.get(1.0,END)
            secret =lsb.hide(str(filename), message)

        def Show():
            clear_message = lsb.reveal(filename)
            text1.delete(1.0,END)
            text1.insert(END,clear_message)

        def save():
            secret.save("secret.png")

        #icon
        image_icon=PhotoImage(file="logo.jpg")
        stg.iconphoto(False,image_icon)

        #logo
        logo=PhotoImage(file="logo.png")
        Label(stg,image=logo,bg="#008080").place(x=10,y=0)

        Label(stg,text="IMAGE STEGANOGRAPHY SYSTEM",bg="#008080",fg="white",font=('Microsoft YaHei UI Light', 25, 'bold')).place(x=100,y=20)

        #first Frame
        f=Frame(stg,bd=3,bg="black",width=340,height=280,relief=GROOVE)
        f.place(x=10,y=80)

        lbl=Label(f,bg="black")
        lbl.place(x=40,y=10)

        #second Frame
        frame2=Frame(stg,bd=3,width=340,height=280,bg="white",relief=GROOVE)
        frame2.place(x=350,y=80)

        text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
        text1.place(x=0,y=0,width=320,height=295)

        scrollbar1=Scrollbar(frame2)
        scrollbar1.place(x=320,y=0,height=300)

        scrollbar1.configure(command=text1.yview)
        text1.configure(yscrollcommand=scrollbar1.set)

        #third Frame
        frame3=Frame(stg,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
        frame3.place(x=10,y=370)

        Button(frame3, text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
        Button(frame3, text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
        Label(frame3,text="PNG or JPG",bg="#2f4155",fg="yellow").place(x=20,y=5)

        #fourth Frame
        frame4=Frame(stg,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
        frame4.place(x=360,y=370)

        Button(frame4, text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
        Button(frame4, text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
        Label(frame4,text="PNG or JPG",bg="#2f4155",fg="yellow").place(x=20,y=5)


        stg.mainloop()



    else:
        messagebox.showerror('Invalid','Invalid Username or Password')



img = PhotoImage(file='login.png')
Label(root,image=img, bg='white').place(x=50,y=50)

frame=Frame(root,width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)



#Username
def on_enter(e):
    user.delete(0, 'end')

    
def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Username')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)



#Password
def on_enter(e):
    code.delete(0, 'end')

    
def on_leave(e):
    name = code.get()
    if name=='':
        code.insert(0,'Password')


code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)




Button(frame,width=39,pady=7,text='Sign In', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35,y=204)
# label=Label(frame,text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
# label.place(x=75, y=270)

# sign_up = Button(frame, width=6, text='Sign Up' , border=0, bg='white', cursor='hand2', fg ='#57a1f8')
# sign_up.place(x=215,y=270)



root.mainloop()