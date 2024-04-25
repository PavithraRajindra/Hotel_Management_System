from tkinter import *
from tkinter import ttk
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root',database='hm_phvs')
cur=con.cursor()


def viewhistory():
    def refresh():
        pg.destroy()
        viewhistory()
    pg=Tk()
    pg.title("View Customer Stay History")
    pg.geometry("800x600")
    pg.resizable(0, 0)
    pg.configure(bg='sky blue')
    cur.execute("select * from customer")
    ctr=cur.fetchall()
    con.commit()
    Label(pg,bd=4,relief='solid',text = "Customer Stay History",bg='purple',fg ='white',font=("Lucida Calligraphy",20),padx=100,pady=20).pack(side = TOP)
    #Refresh Button
    Button(pg, text = " Refresh ⟳", width = 12,height = 1,command = refresh).pack(side = TOP,anchor = "ne",padx = 20)
    tree=ttk.Treeview(pg,column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show = 'headings')
    tree.column("#1", anchor = CENTER,width = 60)
    tree.heading("#1", text = "Cno")
    tree.column("#2", anchor = CENTER,width = 130)
    tree.heading("#2", text = "Customer Name")
    tree.column("#3", anchor = CENTER,width = 130)
    tree.heading("#3", text = "Email id")
    tree.column("#4", anchor = CENTER,width = 130)
    tree.heading("#4", text = "Room cost/night")
    tree.column("#5", anchor = CENTER,width = 80)
    tree.heading("#5", text = "Checkin")
    tree.column("#6", anchor = CENTER,width = 80)
    tree.heading("#6", text = "Checkout")
    tree.column("#7", anchor = CENTER,width = 80)
    tree.heading("#7", text = "Duration")
    tree.column("#8", anchor = CENTER,width = 100)
    tree.heading("#8", text = "Minibar Facility")    
        
    tree.pack(pady = 100)

    for i in ctr:
        tree.insert("",END,values=i) 
    #Close Button
    Button(pg, text = "Close", font = ("Courier",10), width = 20, height = 2,bd = 5, command = pg.destroy).pack(side = BOTTOM,pady = 10)

    
