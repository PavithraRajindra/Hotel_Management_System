import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root')
cur=con.cursor()
cur.execute("create database if not exists HM_phvs")
cur.execute("use HM_phvs") #database created n in use

cur.execute("create table if not exists Customer(Cno int not null AUTO_INCREMENT, Cname char(40), email char(80), Room int, Checkin date, Checkout date, Duration int, Minibar_Facility int, primary key(Cno))")
cur.execute("alter table Customer auto_increment=1")
con.commit()
import booking
from booking import *
from Admn import *
from ViewCustomers import *
from Invoice import *
#all modules will be imported here
 
from tkinter import*
phvs=Tk()
phvs.title("PHVS Hotel")
phvs.geometry("800x600")

C1=Canvas(phvs,bd=5,bg="pink")#FFD700
C1.pack(expand=True,fill=BOTH)

hf1=Frame(phvs,bg="#a660fc",bd=5)
hf1.place(relx=0.2,rely=0.03,relwidth=0.6,relheight=0.16)

hl=Label(hf1,text="Welcome to PHVS Hotel", bd=3, relief='solid', bg='#a660fc', fg='black', font=('Lucida Calligraphy',25))
hl.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1=Button(phvs,text="Book Room",bg='#7734eb', fg='white',font=('Courier',15), command=add)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

btn2=Button(phvs,text="View Customer Details",bg='#7734eb', fg='white',font=('Courier',15),command=viewhistory)
btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)

btn3=Button(phvs,text="Print Invoice",bg='#7734eb', fg='white',font=('Courier',15),command=prinv)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4=Button(phvs,text="Administration",bg='#7734eb', fg='white',font=('Courier',15),command=pwchk)
btn4.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)

quitBtn=Button(phvs,text="CLOSE",bg='#c2302b', fg='white',font=('Times New Roman',15),command=phvs.destroy)
quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
