from tkinter import *
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="root",charset='utf8',database='hm_phvs')
cur = con.cursor()

#housekeeping records
cur.execute("create table if not exists housekeeping(SNO int(5) primary key,NAME varchar(20),qty int(5))")
cur.execute("insert ignore into housekeeping values(1,'Shampoo',200)")
cur.execute("insert ignore into housekeeping values(2,'Milk Powder',400)")
cur.execute("insert ignore into housekeeping values(3,'coconut oil',100)")
cur.execute("insert ignore into housekeeping values(4,'bedsheets',500)")
cur.execute("insert ignore into housekeeping values(5,'towels',100)")
cur.execute("insert ignore into housekeeping values(6,'bed cover',200)")
cur.execute("insert ignore into housekeeping values(7,'sandals',150)")
cur.execute("insert ignore into housekeeping values(8,'sugar packets',1000)")
con.commit()

#roominventory records
cur.execute("create table if not exists roominventory(sno int(5) primary key,type_of_rooms char(15),number_of_rooms int(5), rooms_available int(5))")
cur.execute("insert ignore into roominventory values(1,'Classic',60,50)")
cur.execute("insert ignore into roominventory values(2,'Queen',80,55)")
cur.execute("insert ignore into roominventory values(3,'Deluxe',60,40)")
con.commit()

#-----UDF------------
def hview(): 
    
    root = Tk()
    root.title("CV")
    root.geometry("800x800")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="light green")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="HOUSE KEEPING", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="SNO\t\t\t\t NAME\t\t\t\t\t QTY",bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    gethousekeeping = "select * from housekeeping"
    try:
        cur.execute(gethousekeeping)
        data=cur.fetchall()
        con.commit()
        for i in data:
            Label(labelFrame, text="%-60s%-75s%-20s"%(i[0],i[1],i[2]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
            con.commit()
            
    except:
        messagebox.showinfo("Error","Failed to fetch records from database")

    quitBtn = Button(root,text="CLOSE",bg='yellow', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

def rview(): 
    root = Tk()
    root.title("CV")
    root.geometry("800x800")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="light green")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="ROOM DETAILS", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="SNO\t\tTYPE OF ROOMS\t\tNUMBER OF ROOMS\tROOMS AVAILABLE",bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getcustomerdetails = "select * from roominventory"
    try:
        cur.execute(getcustomerdetails)
        data=cur.fetchall()
        con.commit()
        for i in data:
            Label(labelFrame, text="%-39s%-45s%-45s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
            con.commit()
            
    except:
        messagebox.showinfo("Error","Failed to fetch records from database")

    quitBtn = Button(root,text="CLOSE",bg='yellow', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    con.commit()
    root.mainloop()    
#-----main program----
'''def main():
    root = Tk()
    root.title("CV")
    root.geometry("800x600")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="lightgreen")
    Canvas1.pack(expand=True,fill=BOTH)

    btn2 = Button(root,text="ROOM INVENTORY",bg='purple', fg='white',font=('Courier',15),command=rview)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="HOUSE KEEPING",bg='purple', fg='white',font=('Courier',15), command=hview)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
'''
