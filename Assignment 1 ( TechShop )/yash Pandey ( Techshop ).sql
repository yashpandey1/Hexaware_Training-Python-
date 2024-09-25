
create database TechShop;
use TechShop;


/*
1. Customers:
• CustomerID (Primary Key)
• FirstName
• LastName
• Email
• Phone
• Address
*/
create table Customers(
CustomerID int Identity Primary Key,
FirstName varchar(30),
LastName varchar(30),
Email varchar(30),
Phone varchar(30),
Address varchar(40)
);


/*
2. Products:
• ProductID (Primary Key)
• ProductName
• Description
• Price

*/
create table Products(
ProductID int Identity Primary Key,
ProductName varchar(30),
Description varchar(80),
Price int
);


/*
3. Orders:
• OrderID (Primary Key)
• CustomerID (Foreign Key referencing Customers)
• OrderDate
• TotalAmount
*/
create table Orders(
OrderID int Identity Primary Key,
CustomerID int Foreign key references Customers(CustomerID),
OrderDate date,
TotalAmount int
);


/*
4. OrderDetails:
• OrderDetailID (Primary Key)
• OrderID (Foreign Key referencing Orders)
• ProductID (Foreign Key referencing Products)
• Quantity
*/
create table OrderDetails(
OrderDetailID int Identity Primary key,
OrderID int foreign key references Orders(OrderID),
ProductID int foreign key references Products(ProductID),
Quantity int
);


/*
5. Inventory
• InventoryID (Primary Key)
• ProductID (Foreign Key referencing Products)
• QuantityInStock
• LastStockUpdate
*/
create table Inventory(
InventoryID int Identity Primary key,
ProductID int foreign key references Products(ProductID),
QuantityInStock int,
LastStockUpdate date
);

INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES
( 'Rahul', 'Sharma', 'rahul.sharma@gmail.com', '9876543210', 'Delhi, India'),
( 'Anjali', 'Verma', 'anjali.verma@yahoo.com', '9898989898', 'Mumbai, India'),
( 'Rakesh', 'Mehta', 'rakesh.mehta@gmail.com', '9876501234', 'Bangalore, India'),
( 'Priya', 'Singh', 'priya.singh@hotmail.com', '9823456789', 'Chennai, India'),
( 'Rajesh', 'Gupta', 'rajesh.gupta@outlook.com', '9801234567', 'Kolkata, India'),
( 'Suresh', 'Patel', 'suresh.patel@gmail.com', '9834567890', 'Ahmedabad, India'),
( 'Vikas', 'Chopra', 'vikas.chopra@yahoo.com', '9845671234', 'Hyderabad, India'),
( 'Neha', 'Jain', 'neha.jain@gmail.com', '9887654321', 'Pune, India'),
( 'Amit', 'Kumar', 'amit.kumar@hotmail.com', '9798989898', 'Jaipur, India'),
( 'Sneha', 'Rao', 'sneha.rao@gmail.com', '9878765432', 'Goa, India');

INSERT INTO Products ( ProductName, Description, Price) VALUES
( 'Laptop', 'Dell Inspiron 15 5000', 55000),
( 'Smartphone', 'Samsung Galaxy M31', 17000),
( 'Headphones', 'Sony WH-1000XM4', 25000),
( 'Washing Machine', 'LG 7 kg Fully-Automatic', 30000),
( 'Refrigerator', 'Samsung 253L Frost Free', 27000),
( 'Air Conditioner', 'Daikin 1.5 Ton Inverter', 45000),
( 'Microwave Oven', 'IFB 23L Convection', 12000),
( 'Television', 'Sony 55 inch 4K LED', 80000),
( 'Tablet', 'Apple iPad 10.2 inch', 30000),
( 'Smartwatch', 'Apple Watch Series 6', 40000);

INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES
(1, '2024-09-01', 55000),
(2, '2024-09-05', 17000),
(3, '2024-09-08', 25000),
(4, '2024-09-10', 80000),
(5, '2024-09-12', 45000),
(6, '2024-09-15', 12000),
(7, '2024-09-18', 30000),
(8, '2024-09-20', 27000),
(9, '2024-09-22', 30000),
(10, '2024-09-25', 40000);

INSERT INTO OrderDetails ( OrderID, ProductID, Quantity ) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 2),
(4, 8, 1),
(5, 6, 2),
(6, 7, 1),
(7, 9, 2),
(8, 5, 1),
(9, 4, 2),
(10, 10, 1);

INSERT INTO Inventory ( ProductID, QuantityInStock, LastStockUpdate) VALUES
(1, 50, '2024-08-30'),
(2, 200, '2024-08-30'),
(3, 150, '2024-08-30'),
(4, 80, '2024-08-30'),
(5, 120, '2024-08-30'),
(6, 60, '2024-08-30'),
(7, 90, '2024-08-30'),
(8, 30, '2024-08-30'),
(9, 100, '2024-08-30'),
(10, 75, '2024-08-30');


-- TASK 2


/*
1. Write an SQL query to retrieve the names and emails of all customers.*/

select (FirstName + ' '  + LastName) as Name , Email from Customers;




/*
2. Write an SQL query to list all orders with their order dates 
and corresponding customernames.
*/

SELECT 
    OrderID,
    OrderDate,
    FirstName + ' ' + LastName AS CustomerName
FROM 
    Orders, Customers
where
    Orders.CustomerID = Customers.CustomerID;


/*
3. Write an SQL query to insert a new customer record into the "Customers" table. 
Include customer information such as name, email, and address.
*/


insert into Customers (FirstName, LastName, Email, Address)
values('Yash', 'Pandey', 'yyashp381@gmail.com', 'Bareilly, India');

/*
4. Write an SQL query to update the prices of all electronic gadgets in the
"Products" table by increasing them by 10%.
*/
update Products set Price = Price*1.10;

/*

5. Write an SQL query to delete a specific order and its associated order details from the
"Orders" and "OrderDetails" tables. Allow users to input the order ID as a parameter.

*/
declare @OrderID int = 4;

delete from OrderDetails where OrderID = @OrderID;
delete from Orders where OrderID=@OrderID;

/*

6.Write an SQL query to insert a new order into the "Orders" table. Include the customer ID,
order date, and any other necessary information.

*/
insert into Orders values(1 , '2024-09-30', 5000);

/*
7.Write an SQL query to update the contact information (e.g., email and address) of a specific
customer in the "Customers" table. Allow users to input the customer ID and new contact
information.
*/
declare @CustomerID int = 2;
declare @new_email varchar(30) = 'abc@gmail.com';
declare @new_address varchar(40) = ' Delhi, India';

update Customers
set Email = @new_email , Address = @new_address
where CustomerID = @CustomerID;

/*

8. Write an SQL query to recalculate and update the total cost
of each order in the "Orders" table based on the prices and 
quantities in the "OrderDetails" table.

*/

UPDATE Orders
SET TotalAmount = (
 SELECT (Quantity * Products.Price)
 FROM OrderDetails
 JOIN Products ON OrderDetails.ProductID = Products.ProductID
 WHERE OrderDetails.OrderID = Orders.OrderID);
select * from orders;



/*
9.Write an SQL query to delete all orders and their associated order details for a specific
customer from the "Orders" and "OrderDetails" tables. Allow users to input the customer ID
as a parameter.

*/

declare @Customer_ID int = 1;
DELETE FROM OrderDetails
WHERE OrderID IN (
    SELECT OrderID
    FROM Orders
    WHERE CustomerID = @Customer_ID -- Replace 1 with the specific CustomerID
);

delete from Orders
where CustomerID = @Customer_ID;


/*
10.Write an SQL query to insert a new electronic gadget product into the "Products" table,
including product name, category, price, and any other relevant details
*/
insert into Products values('Mobile Phone' , 'IPhone 15' , 75000); 


/*
11. Write an SQL query to update the status of a specific order
in the "Orders" table (e.g., from "Pending" to "Shipped"). 
Allow users to input the order ID and the new status.
*/
alter table Orders
add Status varchar(20);

declare @Order_ID int = 2;
update Orders
set Status = 'Shipped'
where OrderID = @Order_ID;

select * from Orders;

/*
12. Write an SQL query to calculate and update the 
number of orders placed by each customer in the 
"Customers" table based on the data in the "Orders" table
*/
alter table Customers
add Order_Placed int;

UPDATE Customers
SET Order_Placed = (
    SELECT COUNT(*)
    FROM Orders
    WHERE Orders.CustomerID = Customers.CustomerID
);
select * from Customers;


                          --TASK 3

/*

1. Write an SQL query to retrieve a list of all orders along with customer
information (e.g., customer name) for each order.

*/
select ( FirstName + ' ' +LastName ) as Name, Email, Phone, OrderDate
from Customers join Orders
on Orders.CustomerID = Customers.CustomerID;

/*

2. Write an SQL query to find the total revenue generated by 
each electronic gadget product.Include the product name and the total revenue.

*/
select ProductName, SUM(Price) as Total_Revenue
from Products
group by(ProductName);

/*
3. Write an SQL query to list all customers who have made 
at least one purchase. Include their names and 
contact information.
*/

select ( FirstName + ' ' +LastName ) as Name, Email, Phone
from Customers join Orders
on Orders.CustomerID = Customers.CustomerID;

/*
4. Write an SQL query to find the most popular electronic 
gadget, which is the one with the highest total quantity
ordered.Include the product name and the total quantity ordered.
*/
select top 1 
ProductName, max(Quantity)
from Products join OrderDetails
on Products.ProductID = OrderDetails.ProductID
group by (ProductName);

--5. Write an SQL query to retrieve a list of electronic gadgets along with their corresponding
--categories
ALTER TABLE Products
ADD Categories VARCHAR(255);
UPDATE Products 
SET Categories = 
	CASE 
    WHEN ProductName IN ('Laptop', 'Tablet', 'Smartphone') THEN 'Electronics'
    WHEN ProductName IN ('Headphones', 'Wireless Mouse', 'Mechanical Keyboard', 'Bluetooth Earbuds') THEN 'Accessories'
    WHEN ProductName = 'Monitor' THEN 'Displays'
    WHEN ProductName = 'External SSD' THEN 'Storage'
    WHEN ProductName = 'Portable Charger' THEN 'Power'
    WHEN ProductName = 'Smart Speaker' THEN 'Smart Home'
    WHEN ProductName = 'Smartwatch' THEN 'Wearables'
    WHEN ProductName = 'VR Headset' THEN 'Gaming'
    WHEN ProductName = 'Gaming Console' THEN 'Gaming'
    WHEN ProductName = 'Smart Home Hub' THEN 'Smart Home'
    WHEN ProductName = 'Drone' THEN 'Drones'
    WHEN ProductName = 'Fitness Band' THEN 'Wearables'
    WHEN ProductName = 'Camera' THEN 'Cameras'
    WHEN ProductName = 'Smart Thermostat' THEN 'Smart Home'
    WHEN ProductName = 'E-reader' THEN 'Electronics'
    ELSE 'Other'
END;
SELECT ProductName, Categories from Products Where Categories = 'Electronics';


/*
6. Write an SQL query to calculate the average order 
value for each customer. Include the customer's name 
and their average order value
*/

Select (c.FirstName+' '+c.LastName) as 'CustomerName',
avg(o.TotalAmount) as TotalAvgValue
from Customers c
join Orders o on c.CustomerID = o.CustomerID
group by (c.FirstName+' '+c.LastName);

/*
7. Write an SQL query to find the order with the 
highest total revenue. Include the order ID,
customer information, and the total revenue
*/

select top 1 
o.TotalAmount as HighestRenue,
c.FirstName+' '+c.LastName as 'Name',
c.Email, c.Phone, c.Address
from Orders o join Customers c
on o.CustomerID = c.CustomerID
order by o.TotalAmount desc;

/*
8. Write an SQL query to list electronic gadgets 
and the number of times each product has been
ordered.
*/

Select 
p.ProductID, p.ProductName, COUNT(od.OrderID) AS NumberOfOrders
From Products p
Left Join  OrderDetails as od ON p.ProductID = od.ProductID
WHERE p.Categories = 'Electronics'
GROUP BY
P.ProductID  , p.ProductName;

/*
9. Write an SQL query to find customers who have 
purchased a specific electronic gadget product.
Allow users to input the product name as a parameter.
*/

DECLARE @NameOfProduct VARCHAR(255) = 'Electronics';  
SELECT c.FirstName + ' '+ c.LastName as CustomerName,
c.CustomerID
from CUSTOMERS c

Join Orders as o ON c.CustomerID = o.CustomerID
Join OrderDetails as od ON od.OrderID  = o.OrderID
Join Products as p ON p.ProductID = od.ProductID
where p.Categories = @NameOfProduct;

/*
10. Write an SQL query to calculate the total revenue 
generated by all orders placed within a specific time 
period.Allow users to input the start and end dates as parameters.
*/

DECLARE @STARTDATE DATE = '2020-06-01';
DECLARE  @ENDDATE DATE = '2024-09-22';

Select SUM(TotalAmount) as TotalRevenue
From 
Orders
Where 
OrderDate Between @STARTDATE and @ENDDATE

                    
					           --TASK 4


--1. Write an SQL query to find out which 
--customers have not placed any orders.

SELECT FirstName, LastName 
FROM Customers 
WHERE CustomerID NOT IN (
    SELECT CustomerID FROM Orders
);

--2. Write an SQL query to find the total number
--   of products available for sale. 

SELECT COUNT(*) AS TotalProducts 
FROM Products;


-- 3. Write an SQL query to calculate the total revenue generated by TechShop. 

SELECT SUM(TotalAmount) AS TotalRevenue 
FROM Orders;


/*
4. Write an SQL query to calculate the average 
quantity ordered for products in a specific category.
Allow users to input the category name as a parameter.

*/

declare @inputCategory varchar(20) = 'Electronics';

SELECT AVG(od.Quantity) AS AverageQuantity
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Categories = @inputCategory; 

/*
5. Write an SQL query to calculate the total revenue
generated by a specific customer. Allow users
to input the customer ID as a parameter.

*/

declare @Customerid int = 1;
SELECT SUM(o.TotalAmount) AS TotalCustomerRevenue
FROM Orders o
WHERE o.CustomerID = @Customerid;

/*
6. Write an SQL query to find the customers who
have placed the most orders. List their names
and the number of orders they've placed.
*/

SELECT top 1
c.FirstName+' '+ c.LastName, COUNT(o.OrderID) AS OrderCount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName+' '+c.LastName
ORDER BY OrderCount DESC;

/*
	7. Write an SQL query to find the most popular product
	category, which is the one with the highest
	total quantity ordered across all orders.
	*/
	SELECT top 1
	p.Categories, SUM(od.Quantity) AS TotalQuantity
	FROM Products p
	JOIN OrderDetails od ON p.ProductID = od.ProductID
	GROUP BY p.Categories
	ORDER BY TotalQuantity DESC;

/*
8. Write an SQL query to find the customer who has 
spent the most money (highest total revenue)
on electronic gadgets. List their name and total spending.

*/
SELECT top 1
c.FirstName+' '+ c.LastName Name, SUM(o.TotalAmount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Categories = 'Electronics'
GROUP BY c.FirstName+' '+ c.LastName
ORDER BY TotalSpent DESC;

/*
9. Write an SQL query to calculate the average order value
(total revenue divided by the number of
orders) for all customers.
*/
SELECT AVG(o.TotalAmount) AS AverageOrderValue
FROM Orders o;

/*
10. Write an SQL query to find the total number of 
orders placed by each customer and list their
names along with the order count.
*/
SELECT c.FirstName+' '+ c.LastName Name, COUNT(o.OrderID) AS OrderCount
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName+' '+ c.LastName;



