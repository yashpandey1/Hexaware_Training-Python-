CREATE DATABASE PayXpert;
use PayXpert;

CREATE TABLE Employee (
    EmployeeID INT IDENTITY PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15) NOT NULL,
    Address TEXT NOT NULL,
    Position VARCHAR(50) NOT NULL,
    JoiningDate DATE NOT NULL,
    TerminationDate DATE
);

select * from Payroll
select * from Employee
select * from FinancialRecord
select * from Tax

CREATE TABLE Payroll (
    PayrollID INT IDENTITY PRIMARY KEY,
    EmployeeID INT,
    PayPeriodStartDate DATE NOT NULL,
    PayPeriodEndDate DATE NOT NULL,
    BasicSalary DECIMAL(10, 2) NOT NULL,
    OvertimePay DECIMAL(10, 2) DEFAULT 0.00,
    Deductions DECIMAL(10, 2) DEFAULT 0.00,
    NetSalary DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE Tax (
    TaxID INT IDENTITY PRIMARY KEY,
    EmployeeID INT,
    TaxYear INT NOT NULL,  -- Use INT to store the year
    TaxableIncome DECIMAL(10, 2) NOT NULL,
    TaxAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE FinancialRecord (
    RecordID INT IDENTITY PRIMARY KEY,
    EmployeeID INT,
    RecordDate DATE NOT NULL,
    Description VARCHAR(255) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    RecordType VARCHAR(50) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
