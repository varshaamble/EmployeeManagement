from tkinter import*
from tkinter import messagebox
import pymysql 
import time 
from tkinter import Tk, Label
from tkinter import Toplevel, Label, Scrollbar, BOTH, X, Y, RIGHT, BOTTOM, TOP
from tkinter import ttk
from datetime import datetime  
from tkcalendar import Calendar  
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import reportlab
from fpdf import FPDF
import tkinter as tk  
from tkinter import ttk, messagebox  
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from tkcalendar import DateEntry
#new Trial Code
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Data")
        self.root.geometry("1910x1000+0+0")
        self.root.config(bg="white")
        self.title=Label(self.root,text="Employee Details",font=("times new roman",30,"bold"),bg="#262626",fg="white").place(x=0,y=0,relwidth=1)
        btn_show = Button(self.root, text="All Employees", command=self.allempframe, font=("times new roman", 15), bg="blue", fg="white")
        btn_show.place(x=1280, y=4)
        self.month_var = tk.StringVar()
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.month_combo = ttk.Combobox(self.root, textvariable=self.month_var, values=months, state='readonly', font=("times new roman", 15))
        self.month_combo.set("Select Month")
        self.month_combo.place(x=1426, y=6)  
        btn_show = Button(self.root, text="Monthly Salary", command=self.MonthlySalary, font=("times new roman", 15), bg="blue", fg="white")
        btn_show.place(x=1660, y=4)
        self.var_empcode=StringVar() 
        self.var_empname=StringVar()
        self.var_designation=StringVar()
        self.var_location=StringVar()
        self.var_dept=StringVar()
        self.var_grade=StringVar()
        self.var_panNo=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_Contact=StringVar()        
        self.var_joinDate=StringVar()
        self.var_esicNo=StringVar()
        self.var_uanNo=StringVar()
        self.var_pfNo=StringVar()
        self.var_bankName=StringVar()
        self.var_bankaccNo=StringVar()

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=20,y=80,width=1000,height=880)
        self.title1=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightblue",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        self.lbl_code=Label(Frame1,text="Employee Code: ",font=("times new roman",20),bg="white",fg="black").place(x=0,y=80)
        self.txt_code=Entry(Frame1,font=("times new roman",15),textvariable=self.var_empcode,bg="lightyellow",fg="black")
        self.txt_code.place(x=200,y=84,width=200)

        self.lbl_empName=Label(Frame1,text="Employee Name:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=150)
        self.txt_empname=Entry(Frame1,font=("times new roman",15),textvariable=self.var_empname,bg="lightyellow",fg="black").place(x=200,y=154,width=400)

        self.lbl_designation=Label(Frame1,text="Designation :",font=("times new roman",20),bg="white",fg="black").place(x=0,y=210)
        self.txt_designation=Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=200,y=214,width=200)
        self.lbl_location=Label(Frame1,text="Location :",font=("times new roman",20),bg="white",fg="black").place(x=550,y=210)
        self.txt_location=Entry(Frame1,font=("times new roman",15),textvariable=self.var_location,bg="lightyellow",fg="black").place(x=780,y=214,width=200)

        self.lbl_dept=Label(Frame1,text="Department :",font=("times new roman",20),bg="white",fg="black").place(x=0,y=275)
        self.txt_dept=Entry(Frame1,font=("times new roman",15),textvariable=self.var_dept,bg="lightyellow",fg="black").place(x=200,y=279,width=200)      
        self.lbl_grade=Label(Frame1,text="Grade:",font=("times new roman",20),bg="white",fg="black").place(x=550,y=275)
        self.txt_grade=Entry(Frame1,font=("times new roman",15),textvariable=self.var_grade,bg="lightyellow",fg="black").place(x=780,y=279,width=200)

        self.lbl_panNo=Label(Frame1,text="Pan No :",font=("times new roman",20),bg="white",fg="black").place(x=0,y=340)
        self.txt_panNo=Entry(Frame1,font=("times new roman",15),textvariable=self.var_panNo,bg="lightyellow",fg="black").place(x=200,y=344,width=200)

        self.lbl_Email=Label(Frame1,text="Email:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=405)
        self.txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=200,y=409,width=340)      
        self.lbl_Contact_no=Label(Frame1,text="Contact No:",font=("times new roman",20),bg="white",fg="black").place(x=550,y=405)
        self.txt_Contact_no=Entry(Frame1,font=("times new roman",15),textvariable=self.var_Contact,bg="lightyellow",fg="black").place(x=780,y=409,width=200)

        self.lbl_Address=Label(Frame1,text="Address :",font=("times new roman",20),bg="white",fg="black").place(x=0,y=480)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=200,y=484,width=726,height=50)
                  
        self.lbl_esicNo=Label(Frame1,text="ESIC No:",font=("times new roman",20),bg="white",fg="black").place(x=510,y=568)
        self.txt_esicNo=Entry(Frame1,font=("times new roman",15),textvariable=self.var_esicNo,bg="lightyellow",fg="black").place(x=720,y=572,width=240)

        self.lbl_uanNo=Label(Frame1,text="UAN No:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=638)
        self.txt_uanNo=Entry(Frame1,font=("times new roman",15),textvariable=self.var_uanNo,bg="lightyellow",fg="black").place(x=200,y=642,width=200)                        
        self.lbl_pfNo=Label(Frame1,text="PF Account No:",font=("times new roman",20),bg="white",fg="black").place(x=510,y=638)
        self.txt_pfNo=Entry(Frame1,font=("times new roman",15),textvariable=self.var_pfNo,bg="lightyellow",fg="black").place(x=720,y=642,width=240)

        self.lbl_bankName=Label(Frame1,text="Bank Name:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=705)
        self.txt_bankName=Entry(Frame1,font=("times new roman",15),textvariable=self.var_bankName,bg="lightyellow",fg="black").place(x=200,y=709,width=200)                        
        self.lbl_bankaccNo=Label(Frame1,text="Bank Account No:",font=("times new roman",20),bg="white",fg="black").place(x=510,y=705)
        self.txt_bankaccNo=Entry(Frame1,font=("times new roman",15),textvariable=self.var_bankaccNo,bg="lightyellow",fg="black").place(x=720,y=709,width=240)

        self.lbl_dob = Label(Frame1, text="Date of Birth",font=("times new roman",20),bg="white",fg="black").place(x=550,y=340)
        self.entry_dob = DateEntry(Frame1, date_pattern='dd/mm/yyyy',textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=780, y=344, width=100)
         
        self.lbl_joindate = Label(Frame1, text="Join Date",font=("times new roman",20),bg="white",fg="black").place(x=0,y=568)
        self.entry_joindate = DateEntry(Frame1, date_pattern='dd/mm/yyyy',textvariable=self.var_joinDate,bg="lightyellow",fg="black").place(x=200, y=572)

        self.add_buttonEmpdata = Button(Frame1, text="+", command=self.addEmp, font=("times new roman", 15), bg="blue", fg="white")
        self.add_buttonEmpdata.place(x=560, y=80, width= 40)
        self.btn_searchdataEmpdata = Button(Frame1, text="S", command=self.searchEmp, font=("times new roman", 15), bg="blue", fg="white")
        self.btn_searchdataEmpdata.place(x=640, y=80, width= 40)
        self.btn_ClearEmpdata = Button(Frame1, text="CLR", command=self.clearEmp, font=("times new roman", 15), bg="blue", fg="white")
        self.btn_ClearEmpdata.place(x=720, y=80, width=60)
        self.btn_DeleteEmpdata = Button(Frame1, text="-", command=self.deleteEmp, font=("times new roman", 15), bg="blue", fg="white")
        self.btn_DeleteEmpdata.place(x=820, y=80, width=40)
        self.btn_UpdateEmpdata = Button(Frame1, text="U", command=self.UpdateEmp, font=("times new roman", 15), bg="blue", fg="white")
        self.btn_UpdateEmpdata.place(x=900, y=80, width=40)

        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_minwagesperday=StringVar()
        self.var_presentdays=StringVar()
        self.var_grosssalary=StringVar()
        self.var_Basicda=StringVar()
        self.var_Conveyance=StringVar()
        self.var_HRA=StringVar()
        self.var_Bonus=StringVar()
        self.var_pfEmployee=StringVar()
        self.var_pfEmployer=StringVar()
        self.var_AdminCharges=StringVar()
        self.var_Advance=StringVar()
        self.var_EsicEmployee=StringVar()
        self.var_EsicEmployer=StringVar()
        self.var_ProfessionalTax=StringVar()
        self.var_Deduction=StringVar()
        self.var_NetPay=StringVar()

        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=1040,y=80,width=850,height=880)
        self.title2=Label(Frame2,text="Employee Salary Details",font=("times new roman",20),bg="lightblue",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        self.lblMinWagePerDay=Label(Frame2,text="Per Day Wages :",font=("times new roman",20),bg="white",fg="black").place(x=0,y=80)
        self.txt_MinWagePerDay=Entry(Frame2,font=("times new roman",15),textvariable=self.var_minwagesperday,bg="lightyellow",fg="black").place(x=200,y=84,width=150)        
        self.lblpresentDays=Label(Frame2,text="Present Days:",font=("times new roman",20),bg="white",fg="black").place(x=400,y=80)
        self.txt_presentDays=Entry(Frame2,font=("times new roman",15),textvariable=self.var_presentdays,bg="lightyellow",fg="black").place(x=600,y=84,width=150)

        self.lblgrossSalary=Label(Frame2,text="Gross Salary: ",font=("times new roman",20),bg="white",fg="black").place(x=0,y=150)
        self.txt_grossSalary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_grosssalary,bg="lightyellow",fg="black").place(x=200,y=154,width=150)
        self.lblBasicDA=Label(Frame2,text="Basic + DA :",font=("times new roman",20),bg="white",fg="black").place(x=400,y=150)
        self.txt_BasicDA=Entry(Frame2,font=("times new roman",15),textvariable=self.var_Basicda,bg="lightyellow",fg="black").place(x=600,y=154,width=150)
      
        self.lblConveyance=Label(Frame2,text="Conveyance",font=("times new roman",20),bg="white",fg="black").place(x=0,y=210)
        self.txt_Conveyance=Entry(Frame2,font=("times new roman",15),textvariable=self.var_Conveyance,bg="lightyellow",fg="black").place(x=200,y=214,width=150)
        self.lblHRA=Label(Frame2,text="HRA:",font=("times new roman",20),bg="white",fg="black").place(x=400,y=210)
        self.txt_HRA=Entry(Frame2,font=("times new roman",15),textvariable=self.var_HRA,bg="lightyellow",fg="black").place(x=600,y=214,width=150)
      
        self.lblBonus=Label(Frame2,text="Bonus:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=275)
        self.txt_Bonus=Entry(Frame2,font=("times new roman",15),textvariable=self.var_Bonus,bg="lightyellow",fg="black").place(x=200,y=279,width=150)
        self.lblpfEmployee=Label(Frame2,text="PF Employee:",font=("times new roman",20),bg="white",fg="black").place(x=400,y=275)
        self.txt_pfEmployee=Entry(Frame2,font=("times new roman",15),textvariable=self.var_pfEmployee,bg="lightyellow",fg="black").place(x=600,y=279,width=150)
      
        self.lblpfEmployer=Label(Frame2,text="PF Employer:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=340)
        self.txt_pfEmployer=Entry(Frame2,font=("times new roman",15),textvariable=self.var_pfEmployer,bg="lightyellow",fg="black").place(x=200,y=344,width=150)
        self.lblAdminCharges=Label(Frame2,text="Admin Charges:",font=("times new roman",20),bg="white",fg="black").place(x=400,y=340)
        self.txt_AdminCharges=Entry(Frame2,font=("times new roman",15),textvariable=self.var_AdminCharges,bg="lightyellow",fg="black").place(x=600,y=344,width=150)
      
        self.lblAdvance=Label(Frame2,text="Advance:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=405)
        self.txt_Advance=Entry(Frame2,font=("times new roman",15),textvariable=self.var_Advance,bg="lightyellow",fg="black").place(x=200,y=409,width=150)
        self.lblEsicEmployee=Label(Frame2,text="ESIC Employee:",font=("times new roman",20),bg="white",fg="black").place(x=405,y=405)
        self.txt_EsicEmployee=Entry(Frame2,font=("times new roman",15),textvariable=self.var_EsicEmployee,bg="lightyellow",fg="black").place(x=600,y=409,width=150)
      
        self.lblEsicEmployer=Label(Frame2,text="ESIC Employer:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=480)
        self.txt_EsicEmployer=Entry(Frame2,font=("times new roman",15),textvariable=self.var_EsicEmployer,bg="lightyellow",fg="black").place(x=200,y=484,width=150)
        self.lblProfessionalTax=Label(Frame2,text="Professional Tax:",font=("times new roman",20),bg="white",fg="black").place(x=400,y=480)
        self.txt_ProfessionalTax=Entry(Frame2,font=("times new roman",15),textvariable=self.var_ProfessionalTax,bg="lightyellow",fg="black").place(x=600,y=484,width=150)
      
        self.lblDeduction=Label(Frame2,text="Total Deduction:",font=("times new roman",20),bg="white",fg="black").place(x=0,y=568)
        self.txt_Deduction=Entry(Frame2,font=("times new roman",15),textvariable=self.var_Deduction,bg="lightyellow",fg="black").place(x=200,y=572,width=150)
        self.lblNetPay=Label(Frame2,text="Net Pay:",font=("times new roman",20),bg="white",fg="black").place(x=400,y=568)
        self.txt_NetPay=Entry(Frame2,font=("times new roman",15),textvariable=self.var_NetPay,bg="lightyellow",fg="black").place(x=600,y=572,width=150)
       
        self.btn_search=Button(Frame2,text="Search",command=self.search,font=("times new roman",15),bg="blue",fg="white")
        self.btn_search.place(x=20,y=650,width=200)
        self.btn_Cal=Button(Frame2,text="Cal",command=self.calculate,font=("times new roman",15),bg="blue",fg="white")
        self.btn_Cal.place(x=300,y=650,width=200)
        self.btn_Save=Button(Frame2,text="Save",command=self.save,font=("times new roman",15),bg="blue",fg="white")
        self.btn_Save.place(x=580,y=650,width=200)

        self.btn_Clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",15),bg="blue",fg="white")
        self.btn_Clear.place(x=20,y=730,width=200)
        self.btn_Update=Button(Frame2,text="Update",command=self.Update,font=("times new roman",15),bg="blue",fg="white")
        self.btn_Update.place(x=300,y=730,width=200)
        self.btn_Delete=Button(Frame2,text="Delete",command=self.delete,font=("times new roman",15),bg="blue",fg="white")
        self.btn_Delete.place(x=580,y=730,width=200)

        self.SalarySlip_pdfButton = Button(Frame2, text="Salary Slip", command=self.SalarySlip_pdf,font=("times new roman",15),bg="blue",fg="white")
        self.SalarySlip_pdfButton.place(x=300,y=810,width=200)

    def addEmp(self):
        if not self.var_empcode.get() or not self.var_empname.get() or not self.var_dob.get() or not self.var_joinDate.get():
            messagebox.showerror("Error", "Employee Code, Name, DOB, and Join Date must be provided")
            return
        try:
            dob = self.var_dob.get()  
            join_date = self.var_joinDate.get()  
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()
            cur.execute("SELECT * FROM employeedetails WHERE EmployeeCode = %s", (self.var_empcode.get(),))
            result = cur.fetchone()
            if result:
                messagebox.showerror("Duplicate Entry", "Employee with this Employee Code already exists")
                return            
            cur.execute(
                "INSERT INTO employeedetails (EmployeeCode, EmployeeName, Designation, Location, Department, Grade, PanNo, DateOfBirth, EmailId, ContactNo, Address, JoinDate, ESICNo, UANNo, PFAccountNo, BankName, BankAccountNo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_empcode.get(),
                    self.var_empname.get(),
                    self.var_designation.get(),
                    self.var_location.get(),
                    self.var_dept.get(),
                    self.var_grade.get(),
                    self.var_panNo.get(),
                    dob,  
                    self.var_email.get(),
                    self.var_Contact.get(),
                    self.txt_address.get('1.0', END).strip(),
                    join_date, 
                    self.var_esicNo.get(),
                    self.var_uanNo.get(),
                    self.var_pfNo.get(),
                    self.var_bankName.get(),
                    self.var_bankaccNo.get(),
                )
            )
            con.commit()
            messagebox.showinfo("Success!", "Record successfully saved in the database")
        except pymysql.MySQLError as db_err:
            messagebox.showerror("Database Error", f'Error due to: {str(db_err)}')
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
        finally:
            if con:
                con.close()
            print("Operation complete")

    def searchEmp(self):
        try:
            if hasattr(self, 'tree') and isinstance(self.tree, ttk.Treeview):
                self.tree.delete(*self.tree.get_children())
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()
            cur.execute("SELECT * FROM employeedetails WHERE EmployeeCode=%s", (self.var_empcode.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Emp id", parent=self.root)
            else:
                self.var_empcode.set(row[0])
                self.var_empname.set(row[1])
                self.var_designation.set(row[2])
                self.var_location.set(row[3])
                self.var_dept.set(row[4])
                self.var_grade.set(row[5])
                self.var_panNo.set(row[6])
                self.var_dob.set(row[7])  
                self.var_email.set(row[8])
                self.var_Contact.set(row[9])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END, row[10])
                self.var_joinDate.set(row[11])
                self.var_esicNo.set(row[12])
                self.var_uanNo.set(row[13])
                self.var_pfNo.set(row[14])
                self.var_bankName.set(row[15])
                self.var_bankaccNo.set(row[16])

                self.add_buttonEmpdata.config(state=DISABLED)
                self.btn_UpdateEmpdata.config(state=NORMAL)               
                self.btn_DeleteEmpdata.config(state=NORMAL)          
                self.btn_ClearEmpdata.config(state=NORMAL)   
                self.btn_Update.config(state=NORMAL)  
                self.btn_Save.config(state=NORMAL)     
                self.btn_Delete.config(state=DISABLED)  
                self.btn_search.config(state=NORMAL)
                self.btn_Clear.config(state=NORMAL)
                self.btn_Cal.config(state=NORMAL)
        except pymysql.MySQLError as db_err:
            messagebox.showerror("Database Error", f'Error due to: {str(db_err)}')
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
        finally:
                con.close()  
    def search(self):        
        try:
            if hasattr(self, 'tree') and isinstance(self.tree, ttk.Treeview):
                self.tree.delete(*self.tree.get_children())
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()            
            cur.execute("SELECT EmployeeCode, EmployeeName, Designation, DateOfBirth, JoinDate, ESICNo, UANNo, PFAccountNo, month, year, WagesPerDay, PresentDays, GrossSalary, BasicDA, Conveyance, HRA, Bonus, PFEmployee, PFEmployer, AdminCharges, Advance, ESICEmployee, ESICEmployer, ProfessionalTax, TotalDeduction, NetPay FROM monthlysalary WHERE EmployeeCode=%s", (self.var_empcode.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Emp id", parent=self.root)
            else:
                self.var_empcode.set(row[0])
                self.var_empname.set(row[1])
                self.var_designation.set(row[2])
                self.var_esicNo.set(row[5])
                self.var_uanNo.set(row[6])
                self.var_pfNo.set(row[7])
                self.var_month.set(row[8])
                self.var_year.set(row[9])
                self.var_minwagesperday.set(row[10])
                self.var_presentdays.set(row[11])
                self.var_grosssalary.set(row[12])
                self.var_Basicda.set(row[13])
                self.var_Conveyance.set(row[14])
                self.var_HRA.set(row[15])
                self.var_Bonus.set(row[16])
                self.var_pfEmployee.set(row[17])
                self.var_pfEmployer.set(row[18])
                self.var_AdminCharges.set(row[19])
                self.var_Advance.set(row[20])
                self.var_EsicEmployee.set(row[21])
                self.var_EsicEmployer.set(row[22])
                self.var_ProfessionalTax.set(row[23])
                self.var_Deduction.set(row[24])
                self.var_NetPay.set(row[25])
                self.add_buttonEmpdata.config(state=DISABLED)
                self.btn_UpdateEmpdata.config(state=DISABLED)              
                self.btn_DeleteEmpdata.config(state=DISABLED)        
                self.btn_ClearEmpdata.config(state=NORMAL)   
                self.btn_Update.config(state=NORMAL)   
                self.btn_Save.config(state=DISABLED)    
                self.btn_Delete.config(state=NORMAL)   
                self.btn_searchdataEmpdata.config(state=DISABLED)
                self.btn_Clear.config(state=NORMAL)
                self.btn_Cal.config(state=NORMAL)
        except pymysql.MySQLError as db_err:
            messagebox.showerror("Database Error", f'Error due to: {str(db_err)}')
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
        finally:
            if con:
                con.close()  

    def calculate(self):
        try:
            present_days = self.var_presentdays.get()
            min_wages_per_day = self.var_minwagesperday.get()
            advance = self.var_Advance.get()
            if not present_days or not min_wages_per_day:
                raise ValueError("Present days and minimum wages per day cannot be empty.")
            present_days = int(present_days)
            min_wages_per_day = float(min_wages_per_day)
            advance = float(advance) if advance else 0
            gross_salary = present_days * min_wages_per_day
            self.var_grosssalary.set(str(round(gross_salary, 2)))
            basic_da = gross_salary * 0.6
            conveyance = gross_salary * 0.1
            hra = gross_salary * 0.15
            pf_employee = basic_da * 0.12  
            esic_employee = gross_salary * 0.0075  
            professional_tax = 200  
            bonus = gross_salary - (basic_da + conveyance + hra + pf_employee + esic_employee + professional_tax)
            self.var_Bonus.set(str(round(bonus, 2)))
            self.var_Basicda.set(str(round(basic_da, 2)))
            self.var_Conveyance.set(str(round(conveyance, 2)))
            self.var_HRA.set(str(round(hra, 2)))
            pf_employer = basic_da * 0.12  
            admin_charges = basic_da * 0.01  
            self.var_pfEmployee.set(str(round(pf_employee, 2)))
            self.var_pfEmployer.set(str(round(pf_employer, 2)))
            self.var_AdminCharges.set(str(round(admin_charges, 2)))
            esic_employer = gross_salary * 0.0325
            self.var_EsicEmployee.set(str(round(esic_employee, 2)))
            self.var_EsicEmployer.set(str(round(esic_employer, 2)))
            self.var_ProfessionalTax.set(str(round(professional_tax, 2)))
            total_deductions = pf_employee + esic_employee + advance + professional_tax
            self.var_Deduction.set(str(round(total_deductions, 2)))
            net_pay = gross_salary - total_deductions
            self.var_NetPay.set(str(round(net_pay, 2)))
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def save(self):
        if not self.var_empcode.get() or not self.var_empname.get() or not self.var_dob.get() or not self.var_joinDate.get():
            messagebox.showerror("Error", "Employee Code, Name, DOB, and Join Date must be provided")
            return
        try:
            dob = self.var_dob.get()  
            join_date = self.var_joinDate.get()  
            month = datetime.now().strftime('%B')
            year = datetime.now().year            
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()
            cur.execute(
                "SELECT COUNT(*) FROM monthlysalary WHERE EmployeeCode = %s AND Month = %s AND Year = %s",
                (self.var_empcode.get(), month, year)
            )
            exists = cur.fetchone()[0]
            if exists > 0:
                messagebox.showerror("Error", f"A salary record for {month} {year} already exists for this employee.")
                return
            cur.execute(
                "INSERT INTO monthlysalary (EmployeeCode, EmployeeName, Designation, DateOfBirth, JoinDate, ESICNo, UANNo, PFAccountNo, Month, Year, WagesPerDay, PresentDays, GrossSalary, BasicDA, Conveyance, HRA, Bonus, PFEmployee, PFEmployer, AdminCharges, Advance, ESICEmployee, ESICEmployer, ProfessionalTax, TotalDeduction, NetPay) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",
                (
                    self.var_empcode.get(),
                    self.var_empname.get(),
                    self.var_designation.get(),
                    dob,
                    join_date, 
                    self.var_esicNo.get(),
                    self.var_uanNo.get(),
                    self.var_pfNo.get(),
                    month,  
                    year,  
                    self.var_minwagesperday.get(),
                    self.var_presentdays.get(),
                    self.var_grosssalary.get(),
                    self.var_Basicda.get(),
                    self.var_Conveyance.get(),
                    self.var_HRA.get(),
                    self.var_Bonus.get(),
                    self.var_pfEmployee.get(),
                    self.var_pfEmployer.get(),
                    self.var_AdminCharges.get(),
                    self.var_Advance.get(),
                    self.var_EsicEmployee.get(),
                    self.var_EsicEmployer.get(),
                    self.var_ProfessionalTax.get(),
                    self.var_Deduction.get(),
                    self.var_NetPay.get()
                )
            )
            con.commit()
            messagebox.showinfo("Success!", "Record successfully saved in the database")
        except pymysql.MySQLError as db_err:
            messagebox.showerror("Database Error", f'Error due to: {str(db_err)}')
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
        finally:
            if con:
                con.close()

    def delete(self):
        if self.var_empcode.get() == '':
            messagebox.showerror("Error", "Emp id required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
                cur = con.cursor()
                cur.execute("SELECT * FROM monthlysalary WHERE EmployeeCode=%s", (self.var_empcode.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Emp id", parent=self.root)
                else:
                    op = messagebox.askquestion("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == 'yes':
                        cur.execute("DELETE FROM monthlysalary WHERE EmployeeCode=%s", (self.var_empcode.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Employee record deleted successfully", parent=self.root)
                        self.clear()
                    con.close()
                    self.add_buttonEmpdata.config(state=DISABLED)
                    self.btn_UpdateEmpdata.config(state=DISABLED)               
                    self.btn_DeleteEmpdata.config(state=DISABLED)           
                    self.btn_ClearEmpdata.config(state=DISABLED)   
                    self.btn_searchdataEmpdata.config(state=DISABLED)
                    self.btn_search.config(state=DISABLED)                    
                    self.btn_Update.config(state=NORMAL)   
                    self.btn_Save.config(state=DISABLED)    
                    self.btn_Delete.config(state=NORMAL)   
                    self.btn_Clear.config(state=NORMAL)
                    self.btn_Cal.config(state=NORMAL)
            except pymysql.MySQLError as ex:
                messagebox.showerror("Database Error", f'Error due to: {str(ex)}', parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}', parent=self.root)
            finally:
                if con:
                    con.close()  

    def deleteEmp(self):
        if self.var_empcode.get() == '':
            messagebox.showerror("Error", "Emp id required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
                cur = con.cursor()
                cur.execute("SELECT * FROM employeedetails WHERE EmployeeCode=%s", (self.var_empcode.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Emp id", parent=self.root)
                else:
                    op = messagebox.askquestion("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == 'yes':
                        cur.execute("DELETE FROM employeedetails WHERE EmployeeCode=%s", (self.var_empcode.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Employee record deleted successfully", parent=self.root)
                        self.clearEmp()
                    con.close()
                    self.add_buttonEmpdata.config(state=NORMAL)
                    self.btn_UpdateEmpdata.config(state=NORMAL)                       
                    self.btn_ClearEmpdata.config(state=NORMAL) 
                    self.btn_searchdataEmpdata.config(state=NORMAL)
                    self.btn_search.config(state=DISABLED)
                    self.btn_Update.config(state=DISABLED)   
                    self.btn_Save.config(state=DISABLED)     
                    self.btn_Delete.config(state=DISABLED)    
                    self.btn_Clear.config(state=DISABLED)
                    self.btn_Cal.config(state=DISABLED)                    
            except pymysql.MySQLError as ex:
                messagebox.showerror("Database Error", f'Error due to: {str(ex)}', parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}', parent=self.root)
            finally:
                if con:
                    con.close() 

    def clearEmp(self):
        self.btn_Save.config(state=NORMAL)
        self.btn_Update.config(state=DISABLED)
        self.btn_Delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        self.var_empcode.set('')  
        self.var_empname.set('') 
        self.var_designation.set('') 
        self.var_location.set('')  
        self.var_dept.set('') 
        self.var_grade.set('')  
        self.var_panNo.set('')  
        self.var_dob.set('')  
        self.var_email.set('')  
        self.var_Contact.set('') 
        self.txt_address.delete('1.0', END)          
        self.var_joinDate.set('')          
        self.var_esicNo.set('')  
        self.var_uanNo.set('') 
        self.var_pfNo.set('') 
        self.var_bankName.set('') 
        self.var_bankaccNo.set('')             

    def clear(self):
        self.btn_Save.config(state=NORMAL)
        self.btn_Update.config(state=DISABLED)
        self.btn_Delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        self.var_month.set('')  
        self.var_year.set('') 
        self.var_minwagesperday.set('')  
        self.var_presentdays.set('')  
        self.var_grosssalary.set('')  
        self.var_Basicda.set('')
        self.var_Conveyance.set('') 
        self.var_HRA.set('') 
        self.var_Bonus.set('')  
        self.var_pfEmployee.set('')  
        self.var_pfEmployer.set('') 
        self.var_AdminCharges.set('')  
        self.var_Advance.set('')  
        self.var_EsicEmployee.set('') 
        self.var_EsicEmployer.set('')  
        self.var_ProfessionalTax.set('')  
        self.var_Deduction.set('') 
        self.var_NetPay.set('')  

    def Update(self):
        if not self.var_empcode.get() or not self.var_empname.get() or not self.var_presentdays.get() or not self.var_minwagesperday.get():
            messagebox.showerror("Error", "Employee Code, Name, Present Days, and Minimum Wages per Day must be provided")
            return
        try:
            dob = self.var_dob.get()  
            join_date = self.var_joinDate.get()  
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()
            cur.execute(
                "UPDATE monthlysalary SET EmployeeName=%s, Designation=%s, DateOfBirth=%s, JoinDate=%s, ESICNo=%s, UANNo=%s, PFAccountNo=%s, WagesPerDay=%s, PresentDays=%s, GrossSalary=%s, BasicDA=%s, Conveyance=%s, HRA=%s, Bonus=%s, PFEmployee=%s, PFEmployer=%s, AdminCharges=%s, Advance=%s, ESICEmployee=%s, ESICEmployer=%s, ProfessionalTax=%s, TotalDeduction=%s, NetPay=%s WHERE EmployeeCode=%s",
                (
                    self.var_empname.get(),
                    self.var_designation.get(),
                    dob,
                    join_date, 
                    self.var_esicNo.get(),
                    self.var_uanNo.get(),
                    self.var_pfNo.get(),
                    self.var_minwagesperday.get(),
                    self.var_presentdays.get(),
                    self.var_grosssalary.get(),
                    self.var_Basicda.get(),
                    self.var_Conveyance.get(),
                    self.var_HRA.get(),
                    self.var_Bonus.get(),
                    self.var_pfEmployee.get(),
                    self.var_pfEmployer.get(),
                    self.var_AdminCharges.get(),
                    self.var_Advance.get(),
                    self.var_EsicEmployee.get(),
                    self.var_EsicEmployer.get(),
                    self.var_ProfessionalTax.get(),
                    self.var_Deduction.get(),
                    self.var_NetPay.get(),
                    self.var_empcode.get()  
                )
            )                    
            con.commit()
            messagebox.showinfo("Success", "Record successfully updated")
        except pymysql.MySQLError as db_err:
            messagebox.showerror("Database Error", f'Error due to: {str(db_err)}')
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
        finally:
            if con:
                con.close()
            print("Operation complete")
            
    def UpdateEmp(self):
        if not self.var_empcode.get() or not self.var_empname.get() or not self.var_dob.get() or not self.var_joinDate.get():
            messagebox.showerror("Error", "Employee Code, Name, DOB, and Join Date must be provided")
            return
        try:
            dob = self.var_dob.get()  
            join_date = self.var_joinDate.get()  
            print(f"DOB: {dob}, Join Date: {join_date}")
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()
            cur.execute(
                "UPDATE employeedetails SET EmployeeName=%s, Designation=%s, Location=%s, Department=%s, Grade=%s, PanNo=%s, DateOfBirth=%s, EmailId=%s, ContactNo=%s, Address=%s, JoinDate=%s, ESICNo=%s, UANNo=%s, PFAccountNo=%s, BankName=%s, BankAccountNo=%s WHERE EmployeeCode=%s",
                (
                    self.var_empname.get(),
                    self.var_designation.get(),
                    self.var_location.get(),
                    self.var_dept.get(),
                    self.var_grade.get(),
                    self.var_panNo.get(),
                    dob,  
                    self.var_email.get(),
                    self.var_Contact.get(),
                    self.txt_address.get('1.0', END).strip(),
                    join_date,
                    self.var_esicNo.get(),
                    self.var_uanNo.get(),
                    self.var_pfNo.get(),
                    self.var_bankName.get(),
                    self.var_bankaccNo.get(),
                    self.var_empcode.get()  
                )
            )
            con.commit()
            messagebox.showinfo("Success", "Record successfully updated")
        except pymysql.MySQLError as db_err:
            messagebox.showerror("Database Error", f'Error due to: {str(db_err)}')
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
        finally:
            if con:
                con.close()
            print("Operation complete")
            
    def close_emp_frame(self):
        if self.frame is not None:
            self.frame.destroy() 
            self.frame = None  

    def allempframe(self):
        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=0, y=50, relwidth=1, relheight=10)
        column_widths = {
            "EmployeeCode": 88,
            "EmployeeName": 160,
            "Designation": 120,
            "Location": 50,
            "Department": 80,
            "Grade": 30,
            "PanNo": 90,
            "DateOfBirth": 80,
            "EmailId": 180,
            "ContactNo": 80,
            "Address": 250,
            "JoinDate": 80,
            "ESICNo": 60,
            "UANNo": 100,
            "PFAccountNo": 120,
            "BankName": 60,
            "BankAccountNo": 100
        }
        self.employee_table = ttk.Treeview(self.frame, columns=list(column_widths.keys()), show="headings")
        for col in self.employee_table["columns"]:
            self.employee_table.heading(col, text=col)
            self.employee_table.column(col, width=column_widths[col], anchor="center")
        self.scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.frame, orient=VERTICAL)
        self.employee_table.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.configure(command=self.employee_table.xview)
        self.scroll_y.configure(command=self.employee_table.yview)
        self.employee_table.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.EmpDetailsbtn_save_pdf = Button(self.frame, text="Save as PDF", command=self.EmpDetailssave_as_pdf, font=("times new roman", 15), bg="green", fg="white")
        self.EmpDetailsbtn_save_pdf.pack(pady=10)
        self.btn_close_frame = Button(self.frame, text="Close Frame", command=self.close_emp_frame, font=("times new roman", 15), bg="red", fg="white")
        self.btn_close_frame.pack(pady=10)
        self.fetch_and_display_employees()

    def fetch_and_display_employees(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()
            cur.execute("SELECT * FROM employeedetails")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.employee_table.delete(*self.employee_table.get_children())  
                for row in rows:
                    self.employee_table.insert('', END, values=row)
            con.close()
        except pymysql.MySQLError as db_err:
            messagebox.showerror("Database Error", f"Error due to: {str(db_err)}")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
 
    def EmpDetailssave_as_pdf(self):
        try:
            print("Save as PDF button clicked")
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 10, txt="All Employee Details Report", ln=True, align='C')
            headers = ['EmpCode', 'EmployeeName', 'Designation', 'Location', 'Department', 'Grade', 'PanNo', 'Date Of Birth', 'Email Id', 'Contact No', 'Address', 'Join Date', 'ESIC No', 'UAN No', 'PFAccount No', 'Bank Name', 'Bank Account No']
            header_widths = [10, 28, 15, 12, 12, 8, 12, 14, 25, 12, 40, 12, 12, 12, 24, 15, 22]  
            pdf.set_font("Arial", 'B', size=5)
            for i, header in enumerate(headers):
                pdf.cell(header_widths[i], 9, txt=header, border=1, align='C')
            pdf.ln()
            pdf.set_font("Arial", size=4)
            data_row_height = 4
            for item in self.employee_table.get_children():
                row = self.employee_table.item(item)['values']
                for i, value in enumerate(row):
                    pdf.cell(header_widths[i], data_row_height, txt=str(value), border=1, align='C')
                pdf.ln()
            pdf_file_name = "EmpAllDetails.pdf"
            pdf.output(pdf_file_name)
            messagebox.showinfo("Success", f"PDF saved successfully as {pdf_file_name}!")
        except Exception as e:
            print(f"Error saving PDF: {str(e)}")
            messagebox.showerror("Error", f"Error saving PDF: {str(e)}")

    def MonthlySalary(self):
        if hasattr(self, 'frame'):
            self.frame.destroy()
        selected_month = self.month_var.get()
        if selected_month == "Select Month":
            messagebox.showerror("Error", "Please select a month")
            return
        self.frame = tk.Frame(self.root, bg="lightgrey")
        self.frame.place(x=0, y=50, relwidth=1, relheight=0.8)
        columns = ('EmpCode', 'EmpName', 'UANNo', 'PFNo', 'ESICNo', 'Designation', 'WagesPerDay', 'PresentDays', 'GrossSalary', 'BasicDA', 'Conveyance', 'HRA', 'Bonus', 'PFEmployee', 'PFEmployer', 'AdminCharges', 'ESICEmployee', 'ESICEmployer', 'Advance', 'ProfessionalTax', 'Deduction', 'NetPay')
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')
        headings = {
            'EmpCode': 'Employee Code',
            'EmpName': 'Employee Name',
            'UANNo': 'UAN No',
            'PFNo': 'PF No',
            'ESICNo': 'ESIC No',
            'Designation': 'Designation',
            'WagesPerDay': 'Minimum Wages Per Day',
            'PresentDays': 'Present Days',
            'GrossSalary': 'Gross Salary',
            'BasicDA': 'BASIC+DA',
            'Conveyance': 'Conveyance',
            'HRA': 'HRA',
            'Bonus': 'Bonus',
            'PFEmployee': 'PF Employee',
            'PFEmployer': 'PF Employer',
            'AdminCharges': 'Admin Charges',
            'ESICEmployee': 'ESIC Employee',
            'ESICEmployer': 'ESIC Employer',
            'Advance': 'Advance',
            'ProfessionalTax': 'Professional Tax',
            'Deduction': 'Total Deduction',
            'NetPay': 'Net Pay'
        }
        for col, text in headings.items():
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120) 
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.btn_save_pdf = tk.Button(self.frame, text="Save as PDF", command=self.save_as_pdf, font=("times new roman", 15), bg="green", fg="white")
        self.btn_save_pdf.pack(pady=10)
        self.btn_close_frame = Button(self.frame, text="Close Frame", command=self.close_emp_frame, font=("times new roman", 15), bg="red", fg="white")
        self.btn_close_frame.pack(pady=10)
        self.fetch_employee_data(selected_month)

    def fetch_employee_data(self, selected_month):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='allemployees')
            cur = con.cursor()
            query = """
            SELECT EmployeeCode, EmployeeName, UANNo, PFAccountNo, ESICNo, Designation, WagesPerDay, PresentDays, 
                GrossSalary, BasicDA, Conveyance, HRA, Bonus, PFEmployee, PFEmployer, AdminCharges, 
                 ESICEmployee, ESICEmployer, Advance, ProfessionalTax, TotalDeduction, NetPay 
            FROM monthlysalary 
            WHERE Month=%s
            """
            cur.execute(query, (selected_month,))
            rows = cur.fetchall()
            self.tree.delete(*self.tree.get_children())  
            for row in rows:
                self.tree.insert('', tk.END, values=row)
            con.close()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Error connecting to the database: {str(e)}")
            
    def save_as_pdf(self):
        selected_month = self.month_var.get()
        if selected_month == "Select Month":
            messagebox.showerror("Error", "Please select a month")
            return
        pdf = FPDF(orientation='L', unit='mm', format='A4')  
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(0, 10, txt=f"{selected_month} Salary Report", ln=True, align='C')
        headers = ['EmpCode', 'EmpName', 'UANNo', 'PFNo', 'ESICNo', 'Designation', 'WagesPerDay', 'PresentDays', 'GrossSalary', 'BasicDA', 'Conveyance', 'HRA', 'Bonus', 'PFEmployee', 'PFEmployer', 'AdminCharges', 'ESICEmployee', 'ESICEmployer', 'Advance', 'ProfessionalTax', 'Deduction', 'NetPay']
        header_widths = [9, 25, 10, 20, 10, 20, 14, 12, 11, 10, 12, 8, 8, 12, 12, 15, 14, 14, 9, 15, 10, 10]  
        pdf.set_font("Arial", 'B', size=5)
        for i, header in enumerate(headers):
            pdf.cell(header_widths[i], 9, txt=header, border=1, align='C')
        pdf.ln()
        pdf.set_font("Arial", size=4)
        data_row_height = 4  
        for item in self.tree.get_children():
            row = self.tree.item(item)['values']
            for i, value in enumerate(row):
                pdf.cell(header_widths[i], data_row_height, txt=str(value), border=1, align='C')
            pdf.ln()
        pdf_file_name = f"{selected_month}_Salary_Report.pdf"
        pdf.output(pdf_file_name)
        messagebox.showinfo("Success", f"PDF saved successfully as {pdf_file_name}!")

    def SalarySlip_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.set_font("Arial", style='B', size=18)
        pdf.cell(0, 10, txt="Company Name", ln=True, align='C')
        pdf.set_font("Arial", size= 12 )
        pdf.cell(0, 10, txt="Address", ln=False, align='C')
        pdf.ln(8)                  
        pdf.set_font('Arial', 'B', 10)  
        pdf.cell(0, 10, txt=f"PAYSLIP", ln=True, align='C')  
        pdf.ln(12)
        pdf.rect(5, 5, 200, 133)                  
        pdf.line(5, 35, 205, 35)
        label_x1 = 5
        value_x1 = 42  
        colon_x1 = 40
        start_y = 38  
        label_x2 = 105
        value_x2 = 147  
        colon_x2 = 145
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="Employee Name", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_empname.get()}", border=0) 
        pdf.set_xy(label_x2, start_y) 
        pdf.cell(80, 5, txt="Employee Code", border=0)
        pdf.set_xy(colon_x2, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x2, start_y)  
        pdf.cell(100, 5, txt=f"{self.var_empcode.get()}", border=0) 
        pdf.ln(5)  
        start_y += 6
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="Designation", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_designation.get()}", border=0) 
        pdf.set_xy(label_x2, start_y) 
        pdf.cell(80, 5, txt="Department", border=0)
        pdf.set_xy(colon_x2, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x2, start_y)  
        pdf.cell(100, 5, txt=f"{self.var_dept.get()}", border=0) 
        pdf.ln(5)  
        start_y += 6
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="Pan No", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_panNo.get()}", border=0) 
        pdf.set_xy(label_x2, start_y) 
        pdf.cell(80, 5, txt="Bank Name", border=0)
        pdf.set_xy(colon_x2, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x2, start_y)  
        pdf.cell(100, 5, txt=f"{self.var_bankName.get()}", border=0) 
        pdf.ln(5)  
        start_y += 6
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="Bank Account No", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_bankaccNo.get()}", border=0) 
        pdf.set_xy(label_x2, start_y) 
        pdf.cell(80, 5, txt="Grade", border=0)
        pdf.set_xy(colon_x2, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x2, start_y)  
        pdf.cell(100, 5, txt=f"{self.var_grade.get()}", border=0) 
        pdf.ln(5)  
        start_y += 6
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="Present Days", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_presentdays.get()}", border=0) 
        pdf.set_xy(label_x2, start_y) 
        pdf.cell(80, 5, txt="ESIC No", border=0)
        pdf.set_xy(colon_x2, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x2, start_y)  
        pdf.cell(100, 5, txt=f"{self.var_esicNo.get()}", border=0) 
        pdf.ln(5)  
        start_y += 6
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="UAN No", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_uanNo.get()}", border=0) 
        pdf.set_xy(label_x2, start_y) 
        pdf.cell(80, 5, txt="Date of Birth", border=0)
        pdf.set_xy(colon_x2, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x2, start_y)  
        pdf.cell(100, 5, txt=f"{self.var_dob.get()}", border=0) 
        pdf.ln(5)  
        start_y += 6
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="PF No", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_pfNo.get()}", border=0) 
        pdf.set_xy(label_x2, start_y) 
        pdf.cell(80, 5, txt="Join Date", border=0)
        pdf.set_xy(colon_x2, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x2, start_y)  
        pdf.cell(100, 5, txt=f"{self.var_joinDate.get()}", border=0) 
        pdf.ln(5)  
        start_y += 6
        pdf.set_font("Arial", size=10)                
        pdf.set_xy(label_x1, start_y)  
        pdf.cell(80, 5, txt="Month/Year", border=0) 
        pdf.set_xy(colon_x1, start_y)  
        pdf.cell(5, 5, txt=":", border=0) 
        pdf.set_xy(value_x1, start_y)  
        pdf.cell(30, 5, txt=f"{self.var_month.get()} {self.var_year.get()}", border=0) 
        pdf.ln(8)  
        pdf.set_font("Arial", style='B', size=12)
        header_y = 92  
        line_y_offset = 4 
        line_spacing = 0  

        pdf.line(5, header_y - line_y_offset, 205, header_y - line_y_offset)

        pdf.cell(100, 10, txt="Earnings", border=0, align='C', ln=False)
        pdf.cell(100, 10, txt="Deductions", border=0, align='C', ln=False)

        pdf.ln(5)  
        pdf.line(5, header_y + 5, 205, header_y + 5)  
        pdf.ln(5)

        start_y = pdf.get_y()
        cell_height = 8

        earnings = [
            ("Basic + DA", self.var_Basicda.get()),
            ("Conveyance", self.var_Conveyance.get()),
            ("HRA", self.var_HRA.get()),
            ("Attendance Bonus", self.var_Bonus.get()),
        ]
        deductions = [
            ("PF (Employee)", self.var_pfEmployee.get()),
            ("ESIC (Employee)", self.var_EsicEmployee.get()),
            ("Advance", self.var_Advance.get()),
            ("Professional Tax", self.var_ProfessionalTax.get()),
        ]

        pdf.set_font("Arial", size=10)

        start_x = 5
        pdf.set_xy(start_x, start_y)

        line_start_x = 105  
        line_start_y = 88  
        line_length = 50  
        pdf.line(line_start_x, line_start_y, line_start_x, line_start_y + line_length)

        for i in range(max(len(earnings), len(deductions))):
            if i < len(earnings):
                pdf.set_x(5) 
                pdf.cell(40, cell_height, txt=earnings[i][0], border=0, ln=False) 
                pdf.set_x(40)  
                pdf.cell(5, cell_height, txt=":", border=0, ln=False)  
                pdf.set_x(42) 
                pdf.cell(50, cell_height, txt=str(earnings[i][1]), border=0, ln=False)  
            else:
                pdf.cell(100, cell_height, txt="", border=0, ln=False)  

            if i < len(deductions):
                pdf.set_x(105)  
                pdf.cell(40, cell_height, txt=deductions[i][0], border=0, ln=False)  
                pdf.set_x(145)  
                pdf.cell(5, cell_height, txt=":", border=0, ln=False)  
                pdf.set_x(147) 
                pdf.cell(50, cell_height, txt=str(deductions[i][1]), border=0, ln=True)  
            else:
                pdf.cell(100, cell_height, txt="", border=0, ln=True)  

        current_y = 130
        pdf.line(5, current_y, 205, current_y)  
        pdf.set_xy(5, current_y)
        cell_heights = 8  
        pdf.set_font('Arial', 'B', 11)  
        pdf.set_x(5) 
        pdf.cell(40, cell_heights, txt="Gross Amount", border=0, ln=False)  
        pdf.set_x(40) 
        pdf.cell(5, cell_heights, txt=":", border=0, ln=False) 
        pdf.set_x(42)  
        pdf.cell(40, cell_heights, txt=str(self.var_grosssalary.get()), border=0, ln=False)  

        pdf.set_x(105)  
        pdf.cell(40, cell_heights, txt="Total Deduction", border=0, ln=False)  
        pdf.set_x(145) 
        pdf.cell(5, cell_heights, txt=":", border=0, ln=False) 
        pdf.set_x(147)  
        pdf.cell(40, cell_heights, txt=str(self.var_Deduction.get()), border=0, ln=False)    

        current_y += cell_heights          
        pdf.ln(10)    
        current_y = pdf.get_y()
        pdf.set_font('Arial', 'B', 12)  
        pdf.set_x(5) 
        pdf.cell(37, 8, txt="Net Pay", border=1, ln=False)               
        pdf.set_x(42)  
        pdf.cell(62, 8, txt=str(self.var_NetPay.get()), border=1, align='C', ln=False)  

        pdf.ln(5)  
        line_y_position = current_y + 8 + 5  
        pdf.line(5, line_y_position, 205, line_y_position)  
        pdf.set_y(line_y_position) 
        note_x_position = 15  
        pdf.set_font('Arial', size=10)  
        pdf.set_x(note_x_position)  
        pdf.cell(100, 10, txt="Note: This is a computer-generated statement, it does not need any signature", border=0, align='C', ln=False)
            
        save_directory = r'F:\Varsha\SalarySheet\SalaryReceipt'
        os.makedirs(save_directory, exist_ok=True)
        file_name = f"{self.var_empname.get()}_{self.var_month.get()}_{self.var_year.get()}.pdf".replace(" ", "_")
        file_path = os.path.join(save_directory, file_name)
        pdf.output(file_path)
        messagebox.showinfo("Success", f"PDF saved successfully at {file_path}")
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()
