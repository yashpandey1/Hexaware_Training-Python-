use LoanManagementSystem

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY IDENTITY(1,1),  
    name VARCHAR(100) NOT NULL,                
    email VARCHAR(150) NOT NULL UNIQUE, 
    phone VARCHAR(20) NOT NULL,          
    address VARCHAR(255),                      
    credit_score INT NOT NULL                   
);

CREATE TABLE Loan (
    loan_id INT PRIMARY KEY IDENTITY(1,1),           
    customer_id INT FOREIGN KEY REFERENCES Customer(customer_id), 
    principal_amount DECIMAL(18, 2) NOT NULL,        
    interest_rate DECIMAL(5, 2) NOT NULL,            
    loan_term INT NOT NULL,                          
    loan_type VARCHAR(50) , 
    loan_status VARCHAR(50) , -
    property_address VARCHAR(255) NULL,              
    property_value INT NULL,                         
    car_model VARCHAR(100) NULL,                    
    car_value INT NULL                              
);

