from Regsiter import *
from tkinter import *
from Fullscrn import *
from PIL import Image


class blood_bank:
    def __init__(self):
        root = Tk()
        root.geometry("963x749+540+110")
        root.title("Blood Bank")
        root.configure(background="#d9d9d9")

        self.Frame1 = Canvas(root)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(borderwidth="2", background="#BD081C", width=925)
        root.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\icon.ico")






        self.Frame2=Canvas(self.Frame1)
        self.Frame2.place(relx=0.4, rely=0.2,relheight=0.70,relwidth=0.30)
        self.label1=Label(self.Frame2)




        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.30, rely=0.29, height=73, width=150)
        self.Button3.configure(background="#d9d9d9", text="Login",font=("Times", 20), width=400, command=lambda :page(root))
        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.30, rely=0.49, height=73, width=150)
        self.Button4.configure(background="#d9d9d9", text="Register", font=("Times(", 20), width=100, command=lambda :register(root))
        full1=FullScreenApp(root)
        root.mainloop()


if __name__ == '__main__':
    user = blood_bank()