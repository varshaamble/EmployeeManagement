#DataBase Connection:
1) Create a Database names ad 
2) Create Two Tables Table :-
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
