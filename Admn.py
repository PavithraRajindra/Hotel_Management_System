from tkinter import *
from tkinter import messagebox
from Admn_1 import *
from Admn_2 import *

def enter():
    u1=user.get()
    p1=pw.get()
    if u1=='Shivaji' and p1=='Cool':
        page=Tk()
        page.title("Administration")
        page.geometry("800x600")
        Can=Canvas(page,bg='sky blue',bd=5)
        Can.pack(expand=True,fill=BOTH)
        
        fr=Frame(page,bg="pink",bd=5)
        fr.place(relx=0.2,rely=0.03,relwidth=0.6,relheight=0.16)
        
        Lab=Label(fr,text="ADMINISTRATION",bg='pink',fg='purple',font=('Lucida Calligraphy',25))
        Lab.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        btn1=Button(page,text="EMPLOYEES",bg='purple',fg='white',font=('Courier',15),command=MAINPGM)
        btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

        btn2 = Button(page,text="ROOM INVENTORY",bg='purple', fg='white',font=('Courier',15),command=rview)
        btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

        btn3 = Button(page,text="HOUSE KEEPING",bg='purple', fg='white',font=('Courier',15), command=hview)
        btn3.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

        
    else:
        messagebox.showinfo("Error","Username or Password is incorrect")
def pwchk():
    global user,pw
    phvs=Tk()
    phvs.title("Hotel PHVS")
    phvs.geometry("450x300")
    
    username=Label(phvs,text ="Username").place(x=40,y=60)
    user=Entry(phvs,width=30)
    user.place(x=110,y=60)
    
    u_pw=Label(phvs,text="Password").place(x=40,y=100)
    pw=Entry(phvs,show='*', width = 30)
    pw.place(x=110,y=100)
    
    Enter=Button(phvs,text="Enter",command=enter).place(x=40,y=130)

    phvs.mainloop()

