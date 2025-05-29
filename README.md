# EmployeeManagement

**EmployeeManagement** is a simple and efficient Python-based application to manage employee records and automate salary processing. It is designed to help small to medium businesses keep track of employee details and generate salary slips with ease.

## Features

- Add, update, and delete employee records  
- Store employee details such as name, employee code, UAN, PF, ESIC, designation, and more  
- Monthly salary management with salary slip generation in PDF format  
- Handles salary components including earnings, deductions, and net pay calculation  
- Export salary slips and reports for record-keeping  
- User-friendly interface built with Python (Tkinter or CLI depending on your app)  
- Data storage with MySQL (or your preferred database)

## Database Setup

Before running the application, set up the MySQL database and tables:

1. Create a database named `Employee`:

```sql
CREATE DATABASE Employee;
USE Employee;

Create the required tables:
   CREATE TABLE employeedetails (
      EmployeeCode INT(2) AUTO_INCREMENT PRIMARY KEY,
      EmployeeName VARCHAR(255) NOT NULL,
      Designation VARCHAR(50),
      Location VARCHAR(50),
      Department VARCHAR(50),
      Grade VARCHAR(50),
      PanNo VARCHAR(50),
      DateOfBirth CHAR(10),
      EmailId VARCHAR(50),
      ContactNo VARCHAR(15),
      Address VARCHAR(255),
      JoinDate CHAR(10),
      ESICNo VARCHAR(50),    
      UANNo VARCHAR(50),
      PFAccountNo VARCHAR(50),
      BankName VARCHAR(255),
      BankAccountNo VARCHAR(50)  
  );

  CREATE TABLE monthlysalary (
      EmployeeCode INT(2) AUTO_INCREMENT PRIMARY KEY,
      EmployeeName VARCHAR(255) NOT NULL,
      Designation VARCHAR(50),
      DateOfBirth CHAR(10),
      JoinDate CHAR(10),
      ESICNo VARCHAR(50),    
      UANNo VARCHAR(50),
      PFAccountNo VARCHAR(50),
      Month VARCHAR(20) DEFAULT MONTHNAME(CURDATE()), 
      Year INT DEFAULT YEAR(CURDATE()),              
      WagesPerDay DECIMAL(10, 2),
      PresentDays INT,
      GrossSalary DECIMAL(10, 2),
      BasicDA DECIMAL(10, 2),
      Conveyance DECIMAL(10, 2),
      HRA DECIMAL(10, 2),
      Bonus DECIMAL(10, 2),
      PFEmployee DECIMAL(10, 2),
      PFEmployer DECIMAL(10, 2),
      AdminCharges DECIMAL(10, 2),
      Advance DECIMAL(10, 2),
      ESICEmployee DECIMAL(10, 2),
      ESICEmployer DECIMAL(10, 2),
      ProfessionalTax DECIMAL(10, 2),
      TotalDeduction DECIMAL(10, 2),
      NetPay DECIMAL(10, 2)
  );


## Installation
mysql-connector-python
fpdf

1. Clone the repository:

   ```bash
   git clone https://github.com/varshaamble/EmployeeManagement.git
   cd EmployeeManagement

**Run the main script:**
python salary.py


