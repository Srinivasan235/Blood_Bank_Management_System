from tkinter import messagebox
import Regsiter
from Receive import *
from Donate import *
# from Fullscrn import *
import re
import _sqlite3
from Regsiter import *
from Main import*
from Admin import *

def page(a):
    boot = Tk()
    a.destroy()
    boot.title("Blood Bank")
    boot.geometry("963x749+540+100")
    boot.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\icon.ico")

    Frame1 = Frame(boot)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    label2 = Label(Frame1)
    label2.place(relx=0.10, rely=0.15, height=93, width=1000)
    label2.configure(background="#d9d9d9", text="USERLOGIN", font=("Times", 25), width=800)
    l_id = Entry(boot)

    label1 = Label(Frame1)
    label1.place(relx=0.25, rely=0.35, height=33, width=200)
    label1.configure(background="#d9d9d9", text="Username", font=("Times", 25), width=200)
    l_id = Entry(boot)
    l_id.get()
    l_id.place(relx=0.42,rely=0.35,height=33,width=500)


    Pass_label1 = Label(Frame1, background="#d9d9d9", text="Password", fg='black', font=("Times", 25), width=200)
    Pass_label1.place(relx=0.25, rely=0.45, height=33, width=200)
    Password_box = Entry(boot, show="*")
    Password_box.place(relx=0.42,rely=0.45,height=33,width=500)
    Password_box.get()


    Button_submit = Button(Frame1, background="#d9d9d9", text="LOG IN", fg='black', font=("Times", 25), width=200,command=lambda: loginbut(l_id.get(), Password_box.get(), boot))
    Button_submit.place(relx=0.42, rely=0.55, height=43, width=200)
    Button_submit.configure()

    Button1 = Button(Frame1, background="#d9d9d9", text="register", fg='black', font=("Times", 25), width=200,
                           command=lambda: Regsiter.register(boot))
    Button1.place(relx=0.42, rely=0.65, height=43, width=200)
    Button1.configure()


    full7 = FullScreenApp(boot)
    boot.mainloop()


def loginbut(a, b, d):

    if(a=="admin" and b=="werock"):
        admin(d)
    else:

        if not (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", a)):
            window = Tk()
            window.withdraw()
            messagebox.showwarning("popup", "email is invalid")
            window.destroy()


        elif not (re.search("[\w@$&_!]{8,14}", b)):
            window = Tk()
            window.withdraw()
            messagebox.showwarning("popup", "password is weak or too short")
            window.destroy


        else:
            conn = sqlite3.connect("Blood_Bank.db")
            c = conn.cursor()
            c.execute('SELECT * FROM User WHERE Email = ? and password = ?', (a, b))
            data = c.fetchone()
            conn.commit()
            if data != None:
                root1 = Tk()
                d.destroy()
                root1.title("Blood Bank")
                Frame1 = Frame(root1)
                Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
                Frame1.configure(borderwidth="2", background="#BD081C", width=500)
                label2 = Label(Frame1)
                label2.place(relx=0.10, rely=0.15, height=93, width=1000)
                label2.configure(background="#d9d9d9", text="Do You Want To Donate Or Request?", font=("Times", 25),
                                 width=1200)
                Frame2=Frame(Frame1)
                Frame2.place(relx=0.35, rely=0.3, relheight=0.50, relwidth=0.30)

                Button3 = Button(Frame2)
                Button3.place(relx=0.25, rely=0.30, height=53, width=200)
                Button3.configure(background="#d9d9d9", text="Donate", font=("Courier", 25), width=200,
                                  command=lambda: donate(root1,a))
                Button4 = Button(Frame2, background="#d9d9d9", text="Request", fg='black', font=("Courier", 25),
                                 width=200,
                                 command=lambda: receive(root1,a))
                Button4.place(relx=0.25, rely=0.50, height=53, width=200)
                Button4.configure()
                full7 = FullScreenApp(root1)
                root1.mainloop()

            else:
                window = Tk()
                window.withdraw()
                messagebox.showerror("Error", "Account doesnt exist")
                window.destroy