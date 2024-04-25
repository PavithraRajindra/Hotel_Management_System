from tkinter import *
from tkinter import ttk
from datetime import *
from tkinter import messagebox
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root',database='HM_phvs')
cur=con.cursor()
#========variable declaration=======
e=int()
f=int()
delta=int()
#====================================

def create():
   global e,p,q,r,s,t,u,r1,s1,delta,rbc1,cbc1
   p=a.get()#name
   q=b.get()#email
   
   r=str(c.get())#chkindate
   s=str(d.get())#chkoutdate
   try:
      r1=datetime.strptime(r,'%Y/%m/%d').date()
      s1=datetime.strptime(s,'%Y/%m/%d').date()
      cd=True
   except:
      cd=False
   if cd==False:
      messagebox.showwarning("ERROR!!","Please enter valid date")
   if s1<r1:
      messagebox.showwarning("ERROR!!","Checkout date cannot be before Checkin date")
   else:
      delta=((s1-r1).days)+1
   t=e #minibarrate 
   u=f #roomrate
   cur.execute("insert ignore into Customer(Cname,email,room,checkin,checkout,Duration,Minibar_Facility) values('{}','{}',{},'{}','{}',{},{})".format(p,q,u,r1,s1,delta,t))
   con.commit()
   phvs.destroy()
   
def add():
   global a,b,c,d,e,delta,phvs,ch,cur,rbchk,rbc1,cbc1
   phvs=Tk()
   phvs.title("Hotel PHVS")
   phvs.geometry('800x600')


   C1=Canvas(phvs,bd=5,bg="#FFD700")
   C1.pack(expand=True,fill=BOTH)

   hf1=Frame(phvs,bg="#2444e3",bd=5)
   hf1.place(relx=0.2,rely=0.03,relwidth=0.6,relheight=0.16)

   hl=Label(hf1,text="Welcome to PHVS Hotel", bg='black', fg='white', font=('Lucida Calligraphy',25))
   hl.place(relx=0,rely=0, relwidth=1, relheight=1)
   
   LF=Frame(phvs,bg="blue")
   LF.place(relx=0,rely=0.22,relwidth=1,relheight=1)
   
   #Cname
   lb1=Label(LF,text="Name:",font=('Times New Roman',15),bg='white',fg='black')
   lb1.place(relx=0.02,rely=0.43,relwidth=0.15,relheight=0.05)
   a=Entry(LF)
   a.place(relx=0.2,rely=0.43,relwidth=0.3,relheight=0.05)
   
   #Email
   lb2=Label(LF,text="Email id:",font=('Times New Roman',15),bg='white',fg='black')
   lb2.place(relx=0.02,rely=0.56,relwidth=0.15,relheight=0.05)
   b=Entry(LF)
   b.place(relx=0.2,rely=0.56,relwidth=0.3,relheight=0.05)
   
   #checkin
   lb3=Label(LF,text="Check-in date\n(yyyy/mm/dd):",font=('Times New Roman',15),bg='white',fg='black')
   lb3.place(relx=0.55,rely=0.43,relwidth=0.15,relheight=0.1)
   c=Entry(LF)
   c.place(relx=0.73,rely=0.43,relwidth=0.2,relheight=0.1)
   
   #checkout
   lb4=Label(LF,text="Check-out date\n(yyyy/mm/dd):",font=('Times New Roman',15),bg='white',fg='black')
   lb4.place(relx=0.55,rely=0.56,relwidth=0.15,relheight=0.1)
   d=Entry(LF)
   d.place(relx=0.73,rely=0.56,relwidth=0.2,relheight=0.1)
   
   def cb1chk():
       global e
       if cbc1.get()==1:
           e=200    
       elif cbc1.get()==0:
           e=0
           
   #minibar
   cbc1=IntVar(LF)
   cb1=ttk.Checkbutton(LF,text='Check this box if you wish to avail minibar facility (₹200.00)',variable=cbc1,onvalue=1,offvalue=0,command=cb1chk)
   cb1.place(relx=0.02,rely=0.35)
   
   def rbchk():
       global f
       ctr=rbc1.get()
       if ctr==1:
          f=6000
       elif ctr==2:
          f=6400
       elif ctr==3:
          f=7000
       else:
          messagebox.showinfo("No room selected","Please select a room")
              
   #rooms
   rbc1=IntVar(LF)

   #room1
   rb1=Radiobutton(LF,variable=rbc1,value=1,command=rbchk)
   rb1.place(relx=0.02,rely=0.05)
   lb5=Label(LF,bg='light gray',text='CLASSIC - ₹6000/night*\n40-46 sq m, 2 Twin Beds\nWell lit, Oversized work area\nBathtub, shower\n55 inch LCD TV, Free Wi-Fi',font='Gabriola')
   lb5.place(relx=0.07,rely=0.05,relwidth=0.25,relheight=0.29)

   #room2
   rb2=Radiobutton(LF,variable=rbc1,value=2,command=rbchk)
   rb2.place(relx=0.33,rely=0.05)
   lb6=Label(LF,bg='light pink',text='QUEEN - ₹6400/night*\n44-50 sq m, 1 Queen-sized Bed\nWell lit, Oversized work area\nBathtub, shower\n55 inch LCD TV, Free Wi-Fi',font='Gabriola')
   lb6.place(relx=0.38,rely=0.05,relwidth=0.25,relheight=0.29)

   #room3
   rb3=Radiobutton(LF,variable=rbc1,value=3,command=rbchk)
   rb3.place(relx=0.64,rely=0.05)
   lb7=Label(LF,bg='sky blue',text='DELUXE - ₹7000/night*\n70-76 sq m, 1 King-sized Bed\nWell lit, Oversized work area, City view\nBathtub, shower\n55 inch LCD TV, Free Wi-Fi',font='Gabriola')
   lb7.place(relx=0.69,rely=0.05,relwidth=0.299,relheight=0.29)
   
   #text-tax
   t1=Text(LF,height=0,width=9,bg='orange',font=('Gabriola',18))
   t1.place(relx=0.02,rely=0.68)
   t1.insert(END,'* excl. taxes')
   
   #Proceed Button
   ProceedBtn=Button(phvs,text="PROCEED",bg='light green',fg='black',font=('Times New Roman',15),command=create)
   ProceedBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

   #Quit Button
   quitBtn=Button(phvs,text="EXIT",bg='red', fg='black',font=('Times New Roman',15),command=phvs.destroy)
   quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
   con.commit()
   phvs.mainloop()
