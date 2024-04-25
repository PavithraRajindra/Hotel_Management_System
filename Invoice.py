from tkinter import *
from booking import *
from datetime import *
from booking import delta
import os
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root',database='hm_phvs')
cur=con.cursor()

def prinv():
        global x,itm1,row,i,delta,a_n,b_em,c_ramt,d_mini,e_r,root,textarea      
        took=Tk()
        took.geometry('500x300')
        took.title("Fetching Customer Details...")
        canc=Canvas(took,bg='light pink')
        canc.pack(expand=True,fill=BOTH)
        took.resizable(0,0)

        itm1=IntVar()
        itm1=Entry(took)
        itm1.place(relx=0.5,rely=0.4,relwidth=0.3,relheight=0.1)

        b_em=a_n=str()
        c_ramt=e_r=int()
        
        def fetch():
                global x,itm1,row,i,delta,a_n,b_em,c_ramt,d_mini,e_r
                ctr=0
                x=itm1.get()
                cur.execute("select * from customer")
                data=cur.fetchall()
                con.commit()
                for i in data:
                        if str(i[0])==x:
                                ctr+=1
                                a_n=i[1]
                                b_em=i[2]
                                c_ramt=i[3]*i[6]
                                d_mini=i[7]
                                e_r=i[3]
                                Billing()
                        else:
                                continue
                if ctr==0:
                        mbb=messagebox.showwarning("Oh no!","Customer not found!")
                        mbb.destroy()
                        fetch()
        LBB=Label(took,text="Enter Cno to access the required history...",font=('Courier',10),fg='#7734eb')
        LBB.place(relx=0.16,rely=0.2)

        LB=Label(took,text='Cno:',font=('Times new roman',15),relief='groove',bd=3,bg='#7734eb',fg='white')
        LB.place(relx=0.2,rely=0.4,relwidth=0.2,relheight=0.1)

        btnprint=Button(took,text="print",bg='yellow',fg='black',font=('Times New Roman',15),command=fetch)
        btnprint.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

        def Billing():
                global textarea,a_n,b_em,c_ramt,d_mini,e_r,root
                #textarea.insert(END,'\t\t\t\tHotel Invoice')
                root=Tk()
                root.geometry('800x600')
                Canv=Canvas(root,bg='sky blue')
                Canv.pack(expand=True,fill=BOTH)
                root.resizable(0, 0)
                root.title("Invoice")
                root.configure(bg='sky blue')

                F3=Frame(root,bg='sky blue',relief=GROOVE,bd=10)
                F3.place(x=0,y=0,width=800,height=600)
                bill_title=Label(F3,text='INVOICE',font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=BOTH)

                textarea=Text(F3,font="arial 15 bold")
                textarea.pack()
                
                sroom=str()
                if e_r==6000:
                        sroom="Room: Classic"
                elif e_r==6400:
                        sroom="Room: Queen"
                elif e_r==7000:
                        sroom="Room: Deluxe"
                if d_mini!=0:
                        smini="Minibar"
                tot1=(0.12*c_ramt)+c_ramt
                tot2=0
                textarea.insert(END,f'\n\n  Customer Name\t\t:  {a_n}')
                textarea.insert(END,f'\n  Email Id\t\t:  {b_em}')
                dateh=datetime.now()
                textarea.insert(END,f'\n  Date\t\t:  {dateh.strftime("%d/%m/%Y")}\t\t\t Time:  {dateh.strftime("%H:%M:%S")}\n')
                textarea.insert(END,'\n\n  Service\t\t\tAmount\t\t\tTax\t\tTotal')
                textarea.insert(END,'\n--------------------------------------------------------------------------------------------------------------')
                textarea.insert(END,f'\n  {sroom}\t\t\t{c_ramt}\t\t\t{"12%"}\t\t{tot1}')
                if d_mini!=0:
                        smini="Minibar"
                        tot2=(0.05*d_mini)+d_mini
                        textarea.insert(END,f'\n  {smini}\t\t\t{d_mini}\t\t\t{"5%"}\t                 {tot2}')
                textarea.insert(END,'\n--------------------------------------------------------------------------------------------------------------')
                textarea.insert(END,f'\n\nGrand Total\t\t\t\t\t\t\t\t{tot1+tot2}')
                textarea.insert(END,'\n--------------------------------------------------------------------------------------------------------------')

                




