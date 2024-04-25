from tkinter import *
from mysql.connector import Error
import mysql.connector as mysql
import threading
from tabulate import tabulate
from tkinter import ttk
from tkinter import messagebox


# __________________________________
#Colors
mem_bg = "#101820"
mem_fg  =  "#F2AA4C"        
main_bg  =  "#303030"   
main_fg  =  "#688EB3"           
        
# Functions

# Quit Function and Window____________________________________________
def esc_window():
    def close_app():
        db.close()
        quit()
    exit_page  =  Toplevel()
    exit_page.geometry("325x310")
    exit_page.resizable(0, 0)
    Label(exit_page, text = "", bg = '#2D2926').grid(row = 1)
    exit_page.title("Quit Window")
    exit_page.configure(bg = "#2D2926")
    Label(exit_page, text = " ╔══════════╗", bg = '#2D2926',font = "Corbel 18 bold", fg = "red").grid(row = 2)
    Label(exit_page, text = " Are you sure you want to quit?",bg = "#2D2926", fg = "red", font = "Corbel 14 bold").grid(row = 3)
    Label(exit_page, text = " ╚══════════╝", bg = "#2D2926",font = "Corbel 18 bold", fg = "red").grid(row = 4)
    Label(exit_page, text = "", bg = "#2D2926").grid(row = 5)
    yes_button  =  Button(exit_page, text = "YES", fg = "red2", font = "Corbel 10 bold",width = 20, height = 2, bd = 10, command = close_app).grid(row = 6)
    Label(exit_page, text = "", bg = "#2D2926").grid(row = 7)
    no_button  =  Button(exit_page, text = "NO", fg = "green3", font = "Corbel 10 bold",width = 20, height = 2, bd = 10, command = exit_page.destroy).grid(row = 8)

# MEMBERS WINDOW's ALL WINDOWS AND FUNCTION_________________________

# Adding Employee record command and window
def add_member():
    t = "All fields are mandatory"
    def add_member_info():
        cur.execute("select max(employee_id) from employee")
        temp = cur.fetchall()
        temp = temp[0][0]
        if temp == None:
            temp=10000
        temp_new_id = temp+1
        v1 = temp_new_id
        v2 = first_var.get()
        v3 = last_var.get()
        v4 = phone_number_var.get()
        v5 = email_var.get()
        v6 = DOB_var.get()
        v7 = DOJ_var.get()
        v8 = emp_gender_var.get()
        v9 = int(emp_salary_var.get())
        if v1 and v2 and v3 and v4 and v5 and v6 and v7 and v8 and v9 != "":
            sql = "insert into employee values (%s,'%s','%s','%s','%s','%s','%s','%s',%s)" % (v1,v2,v3,v4,v5,v6,v7,v8,v9)
            cur.execute(sql)
            db.commit()
            #id_var.set("")
            first_var.set("")
            last_var.set("")
            phone_number_var.set("")
            email_var.set("")
            DOB_var.set("")
            DOJ_var.set("")
            emp_gender_var.set("")
            emp_salary_var.set("")
            messagebox.showinfo("Add Employee","New Employee added with ID %s"%v1 ,parent = add_member_window)
            add_member_window.destroy()

        else:
            messagebox.showerror("Add Employee","One or more field(s) are empty" ,parent = add_member_window)
    def clear_cmd():
        first_var.set("")
        last_var.set("")
        phone_number_var.set("")
        email_var.set("")
        DOB_var.set("")
        DOJ_var.set("")
        emp_gender_var.set("")
        emp_salary_var.set("")
    add_member_window  =  Toplevel()
    add_member_window.title("Add Employee")
    add_member_window.geometry("400x950")
    add_member_window.resizable(0, 0)
    add_member_window.configure(bg = mem_bg)
    #Title
    Label(add_member_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(add_member_window, text = "  Add Employee",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(add_member_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(add_member_window, text = "", bg = mem_bg).grid(row = 4)
    #Entry declaration
    first_var = StringVar()
    last_var = StringVar()
    phone_number_var = StringVar()
    email_var = StringVar()
    DOB_var = StringVar()
    DOJ_var = StringVar()
    emp_gender_var = StringVar()
    emp_salary_var = StringVar()
    #Error Notice
    Label(add_member_window, text = t, bg = mem_bg,fg = mem_fg).grid(row = 5)#DETAILS ERROR
    Label(add_member_window, text = "", bg = mem_bg).grid(row = 10)
    #First Name Entry
    Label(add_member_window, text = "    Enter First Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 8, sticky = "w")
    first_name_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = first_var).grid(pady = 10,row = 8, sticky = "e"))
    #Last Name Entry
    Label(add_member_window, text = "    Enter Last Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 9, sticky = "w")
    last_name_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = last_var).grid(pady = 10,row = 9, sticky = "e"))
    #Phone Number Entry
    Label(add_member_window, text = "    Enter Phone Number :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 10, sticky = "w")
    phone_number_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = phone_number_var).grid(pady = 10,row = 10, sticky = "e"))
    #Email ID Entry
    Label(add_member_window, text = "    Enter Email ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 11, sticky = "w")
    email_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = email_var).grid(pady = 10,row = 11, sticky = "e"))
    #DOB ID Entry
    Label(add_member_window, text = "    Enter DOB :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 11,row = 12, sticky = "w")
    DOB_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = DOB_var).grid(pady = 10,row = 12, sticky = "e"))
    #DOJ ID Entry
    Label(add_member_window, text = "    Enter DOJ :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 11,row = 13, sticky = "w")
    DOJ_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = DOJ_var).grid(pady = 10,row = 13, sticky = "e"))
    #sal_gender ID Entry
    Label(add_member_window, text = "    Enter Gender:", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 11,row = 14, sticky = "w")
    gender_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = emp_gender_var).grid(pady = 10,row = 14, sticky = "e"))
   #emp_salary ID Entry
    Label(add_member_window, text = "    Enter Salary :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 11,row = 15, sticky = "w")
    sal_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = emp_salary_var).grid(pady = 10,row = 15, sticky = "e"))
   
   #Buttons
    Button(add_member_window, text = "Add Employee", font = "Corbel 10", width = 20,height = 2, bd = 5, command = add_member_info).grid(padx = 25,pady = 15,row = 16,sticky = "w")
    Button(add_member_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = add_member_window.destroy).grid(padx = 15,pady = 17,row = 17)
    Button(add_member_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(padx = 15,pady = 18,row = 16,sticky = "e")

# Delete Employee record command and window    
def delete_member():
    t = "All fields are mandatory"
    def delete_member_info():
        dv1 = emp_id_var.get()
        if dv1 != "":
            dv1 = int(emp_id_var.get())
            sql = "select * from employee WHERE employee_id IN (%s)" % (dv1)
            cur.execute(sql)
            myresult  =  cur.fetchall()
            if myresult != []:
                sql = "delete from employee where employee_id = %s" % (dv1)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo("Employee","Employee Deleted with ID %s"%dv1 ,parent = delete_member_window)
                delete_member_window.destroy()
            else:
                messagebox.showerror("Delete Employee","Employee ID does not exist",parent = delete_member_window)
        else:
            messagebox.showerror("Delete Employee","Enter Employee ID",parent = delete_member_window)
    def clear_cmd():
        emp_id_var.set("")
    delete_member_window  =  Toplevel()
    delete_member_window.title("Delete Employee")
    delete_member_window.geometry("400x950")
    delete_member_window.resizable(0, 0)
    delete_member_window.configure(bg = mem_bg)
    #Title
    Label(delete_member_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(delete_member_window, text = "  Delete Employee",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(delete_member_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(delete_member_window, text = "", bg = mem_bg).grid(row = 4)
    #Entry declaration
    emp_id_var = StringVar()
    
    #Error Notice
    Label(delete_member_window, text = t, bg = mem_bg,fg = mem_fg).grid(row = 5)#DETAILS ERROR
    Label(delete_member_window, text = "", bg = mem_bg).grid(row = 10)
	
    #Emp id Entry
    Label(delete_member_window, text = "Enter Emp Id :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 8, sticky = "w")
    emp_id_entry  =  (Entry(delete_member_window, width = 15, font = "Consolas 14",textvariable = emp_id_var).grid(pady = 10,row = 8, sticky = "e"))
    
   #Buttons
    Button(delete_member_window, text = "Delete Employee", font = "Corbel 10", width = 20,height = 2, bd = 5, command = delete_member_info).grid(padx = 25,pady = 15,row = 16,sticky = "w")
    Button(delete_member_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = delete_member_window.destroy).grid(padx = 15,pady = 17,row = 17)
    Button(delete_member_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(padx = 15,pady = 18,row = 16,sticky = "e")
    

# Displaying all employee record
def all_members():
    all_members_window  =  Toplevel()
    all_members_window.title("All Employee Details")
    all_members_window.geometry("1200x475")
    all_members_window.resizable(0, 0)
    all_members_window.configure(bg = mem_bg)
    cur.execute("SELECT * FROM employee")
    myresult  =  cur.fetchall()
    Label(all_members_window, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).pack(side = TOP,pady = 10)
    Label(all_members_window, text = "Employee", bg = mem_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).pack(side = TOP)
    Label(all_members_window, text = " ╚══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).pack(side = TOP)
    #Setting the Table
    tree  =  ttk.Treeview(all_members_window, column = ("c1", "c2", "c3","c4","c5","c6","c7","c8","c9"), show = 'headings')
    tree.column("#1", anchor = CENTER,width = 60)
    tree.heading("#1", text = "Employee. ID")
    tree.column("#2", anchor = CENTER,width = 130)
    tree.heading("#2", text = "First Name")
    tree.column("#3", anchor = CENTER,width = 130)
    tree.heading("#3", text = "Last Name")
    tree.column("#4", anchor = CENTER,width = 100)
    tree.heading("#4", text = "Ph. No.")
    tree.column("#5", anchor = CENTER,width = 130)
    tree.heading("#5", text = "Email ID")
    tree.column("#6", anchor = CENTER,width = 100)
    tree.heading("#6", text = "DOB")
    tree.column("#7", anchor = CENTER,width = 100)
    tree.heading("#7", text = "DOJ")
    tree.column("#8", anchor = CENTER,width = 100)
    tree.heading("#8", text = "Gender")
    tree.column("#9", anchor = CENTER,width = 100)
    tree.heading("#9", text = "Salary")
    
    tree.pack(pady = 20)
    #Appending the records in the table
    for row in myresult:
        tree.insert("", END, values = row) 
    #Close Button
    Button(all_members_window, text = "Close Window", font = "Corbel 10", width = 20, height = 2,bd = 5, command = all_members_window.destroy).pack(side = BOTTOM,pady = 10)


#SEARCH FUNCTION_____________________________________
#Searching by First Name and Last Name
def search_by_name():
    def search_name():
         #Data
        first_name = first_name_var.get()+"%"
        last_name = last_name_var.get()+"%"
        sql = "select * from employee WHERE first_name  like  '%s' and last_name like '%s'" % (first_name, last_name)
        cur.execute(sql)
        myresult  =  cur.fetchall()
        if myresult != []:
            search_result = Toplevel()
            search_result.title("Search Result")
            search_result.geometry("1200x300")
            search_result.resizable(0, 0)
            search_result.configure(bg = mem_bg)
            Label(search_result, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
            Label(search_result, text = "  Result",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
            Label(search_result, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
            Label(search_result, text = "", bg = mem_bg).grid(row = 10)
            #Showing Result
            result  =  Label(search_result, text = tabulate(myresult, headers = ['Emplyee ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','DOB','DOJ','Gender','Salary'], tablefmt = 'fancy_grid'), bg = mem_bg, fg = mem_fg, font = "Consolas 12 ").grid(padx = 20,row = 5)
            Label(search_result, text = "", bg = mem_bg).grid(row = 10)
            Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 10)                                                                                                                 
        else:
            messagebox.showinfo("Search Employee","No Employee found", parent = search_by_ID_window)
    def clear_cmd():
        first_name_var.set("")
        last_name_var.set("")

    first_name_var = StringVar()
    last_name_var = StringVar()
    
    search_by_ID_window  =  Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Employee by Name")
    search_by_ID_window.configure(bg = mem_bg)
    Label(search_by_ID_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(search_by_ID_window, text = "  Search By Name",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_by_ID_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(search_by_ID_window, text = "", bg = mem_bg).grid(row = 4)
    Label(search_by_ID_window, text = "    Enter First Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    #
    first_name_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = first_name_var).grid(row = 5, sticky = "e"))
    Label(search_by_ID_window, text = "    Enter Last Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 6, sticky = "w")
    last_name_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = last_name_var).grid(row = 6, sticky = "e"))
    #
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_by_ID_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_name).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_by_ID_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(search_by_ID_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(search_by_ID_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_ID_window.destroy).grid(row = 9)

    

# Search Employee record Options
def display_members_options():
    display_members_window  =  Toplevel()
    display_members_window.geometry("400x450")
    display_members_window.resizable(0, 0)
    display_members_window.title("Employee Details Options")
    display_members_window.configure(bg = mem_bg)
    Label(display_members_window, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 20).grid(row = 1)
    Label(display_members_window, text = "Search Employee", bg = mem_bg,fg = mem_fg, font = "Corbel 20 bold", padx = 90).grid(row = 2)
    Label(display_members_window, text = " ╚══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 4)
    Button(display_members_window, text = "All Employee", width = 20,height = 2, command = all_members, bd = 5).grid(row = 5)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 6)
    Button(display_members_window, text = "Search By Name", width = 20,height = 2, command = search_by_name, bd = 5).grid(row = 13)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 14)
    Button(display_members_window, text = "Close Window", width = 20,height = 2, command = display_members_window.destroy, bd = 5).grid(row = 15)

#END OF SEARCH FUNCTIONS_______________________________________




# Members Window
def members_window():
    def refresh():
        members_page.destroy()
        members_window()
    members_page  =  Toplevel()
    members_page.geometry("800x500")
    members_page.resizable(0, 0)
    members_page.title("Employee Window")
    members_page.configure(bg = mem_bg)
    # Getting all Employee' records
    cur.execute("SELECT * FROM employee")
    myresult  =  cur.fetchall()
    #Label
    Label(members_page, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).pack(side = TOP,pady = 10)
    Label(members_page, text = "Employee", bg = mem_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).pack(side = TOP)
    Label(members_page, text = " ╚══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).pack(side = TOP)
    Label(members_page,text="To update details,double click the record:",bg=mem_bg,fg=mem_fg,font="Corbel 10").pack(side=TOP,padx=1,pady=1)

    #Refresh Button
    Button(members_page, text = " Refresh ⟳", width = 12,height = 1,command = refresh).pack(side = TOP,anchor = "ne",padx = 20)
    #Setting the Table
    tree  =  ttk.Treeview(members_page, column = ("c1", "c2", "c3","c4","c5","c6","c7","c8","c9"), show = 'headings')
    tree.column("#1", anchor = "w",width = 60)
    tree.heading("#1", text = "Emp. ID")
    tree.column("#2", anchor = "w",width = 100)
    tree.heading("#2", text = "First Name")
    tree.column("#3", anchor = "w",width = 100)
    tree.heading("#3", text = "Last Name")
    tree.column("#4", anchor = "w",width = 100)
    tree.heading("#4", text = "Ph. No.")
    tree.column("#5", anchor = "w",width = 130)
    tree.heading("#5", text = "Email ID")
    tree.column("#6", anchor = "w",width = 60)
    tree.heading("#6", text = "DOB")
    tree.column("#7", anchor = "w",width = 60)
    tree.heading("#7", text = "DOJ")
    tree.column("#8", anchor = "w",width = 60)
    tree.heading("#8", text = "Gender")
    tree.column("#9", anchor = "w",width = 60)
    tree.heading("#9", text = "Salary")
    
    tree.pack(expand = YES,pady = 20)
    #Appending the records in the table
    for row in myresult:
        tree.insert("", END, values = row)
    
    #Members treeview double click event
    def getSelection(event):
        #Function to update from double click event window
        def doubleClickUpdate():
            employee_id = curitem[0]
            pno = phone_number_var.get()
            emid = email_var.get()
            salary = points_var.get()
            if employee_id and pno and emid != "":
                sql = "UPDATE employee SET phone_no = '%s' where employee_id = %s " % (pno,employee_id)
                cur.execute(sql)
                sql = "UPDATE employee SET employee_salary = %s where employee_id = %s " % (salary,employee_id)
                cur.execute(sql)
                sql = "UPDATE employee SET email_id = '%s' where employee_id = %s " % (emid,employee_id)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo("Update Employee Details","Details of Employee with ID %s was updated" % employee_id ,parent = datawindow)
                datawindow.destroy()
                refresh()
            else:
                messagebox.showerror("Update Employee Details", "Phone Number and Email ID are mandatory fields, please fill these fields.")
        
        #getSelection(Datawindow) main code
        currow = tree.focus()
        curitem = (tree.item(currow))['values']
        datawindow = Toplevel()
        datawindow.configure(bg = mem_bg)
        datawindow.geometry("600x550")
        datawindow.resizable(0,0)
        datawindow.title("Employee details edit Window")
        Label(datawindow, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).grid(row = 1,pady = 10)
        Label(datawindow, text = "Employee details", bg = mem_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).grid(row = 2,sticky = 'news')
        Label(datawindow, text = " ╚══════════╝\n", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3, sticky = 'news')
        display_mem = "Employee ID:\t" + str(curitem[0])
        Label(datawindow, text = display_mem, bg = mem_bg,font = "Consolas 16 bold", fg = mem_fg).grid(row = 4, sticky = 'nws',padx = 10)
        Label(datawindow, text = "Name of employee:\t" + curitem[1] + " " + curitem[2] , bg = mem_bg,font = "Consolas 16 bold", fg = mem_fg).grid(row = 5, sticky = 'nws', padx = 10)
        Label(datawindow, text = "" , bg = mem_bg,font = "Consolas 16 bold", fg = mem_fg).grid(row = 6, sticky = 'nws', padx = 10)
    
        phone_number_var = StringVar()
        email_var = StringVar()
        points_var = StringVar()
        #Label and textboxes
        Label(datawindow, text = "Phone Number :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 7, sticky = "w",padx = 10)
        phone_number_entry  =  (Entry(datawindow, width = 20, font = "Consolas 14",textvariable = phone_number_var).grid(pady = 10,row = 7, sticky = "e", padx = 35))
        phone_number_var.set(curitem[3])
        Label(datawindow, text = "Email ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 8, sticky = "w",padx = 10)
        email_entry  =  (Entry(datawindow, width = 20, font = "Consolas 14",textvariable = email_var).grid(pady = 10,row = 8, sticky = "e",padx = 35))
        email_var.set(curitem[4])
        Label(datawindow, text = "Salary :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 9, sticky = "w",padx = 10)
        points_entry  =  (Entry(datawindow, width = 20, font = "Consolas 14",textvariable = points_var).grid(pady = 10,row = 9, sticky = "e",padx = 35))
        points_var.set(curitem[8])
        #Buttons
        Label(datawindow, text = "", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 10, sticky = "w",padx = 10)
        Button(datawindow, text = "Update", font = "Corbel 10", width = 20,height = 2, bd = 5, command = doubleClickUpdate).grid(padx = 25,pady = 15,row = 11,sticky = "w")
        Button(datawindow, text = "Close", font = "Corbel 10", width = 20,height = 2, bd = 5, command = datawindow.destroy).grid(padx = 15,pady = 15,row = 11,sticky = "e")
    #Binding double click event to function
    tree.bind('<Double-1>', getSelection)
    
    # Buttons
    Button(members_page, text = "Search Employee", font = "Corbel 10", width = 20, height = 2,command = display_members_options, bd = 5).pack(side = LEFT ,padx = 30,pady = 5)
    Button(members_page, text = "Add Employee", font = "Corbel 10", width = 20, height = 2,command = add_member, bd = 5).pack(side = LEFT,padx = 30,pady = 5)
    Button(members_page, text = "Delete Employee", font = "Corbel 10" , width = 20, height = 2, command = delete_member, bd = 5).pack(side = LEFT,padx = 30,pady = 5)
    Button(members_page, text = "Close Window", font = "Corbel 10", width = 20, height = 2,bd = 5, command = members_page.destroy).pack(side = RIGHT,padx = 30,pady = 5)
#_________________________________________________________

# Main Window
def MAINPGM():
    main_window  =  Tk()
    main_window.title("Employees - Main Menu")
    main_window.geometry("400x430")
    main_window.resizable(0, 0)
    main_window.configure(bg = main_bg)
    # HEADING
    Label(main_window, text = "EMPLOYEES", bg = main_bg,fg = main_fg, font = "HPSimplifiedReg 20 bold", pady = 25).grid(row = 1)
    Label(main_window, text = "   »»—————　★　—————«« ", bg = main_bg,fg = main_fg, font = "Corbel 20 bold").grid(row = 2)
    # Employee list button
    Label(main_window, text = "", bg = main_bg).grid(row = 3)
    Button(main_window, text = "Employee Info", width = 20, height = 2,command = members_window, bd = 5).grid(row = 4, column = 0)
    # Quit Button
    Label(main_window, text = "", bg = main_bg).grid(row = 9)
    Button(main_window, text = "QUIT", width = 20, height = 2, bd = 5,fg = "red2", command = esc_window).grid(row = 10, column = 0)
    
# __________________________________
# Database startup
t='root'
#___________________________________________________________
  
#qconnect()        
db  =  mysql.connect(host = "localhost", user = "root", passwd = t,database='hm_phvs')
cur  =  db.cursor()

cur.execute("create table if not exists employee(employee_id integer Primary Key, First_name varchar(20) not null, Last_name varchar(20) not null, phone_no char(13) not null unique, Email_ID varchar(35) not null, DOB DATE, DOJ DATE, employee_gender varchar(20) not null, employee_salary integer not null);")
db.commit()

#MAIN  
db  =  mysql.connect(host = "localhost", user = "root", passwd = t,database = "hm_phvs")
cur = db.cursor()

