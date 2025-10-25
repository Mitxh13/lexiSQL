CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2),
    JoinDate DATE
);

INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary, JoinDate)
VALUES 
(1, 'Mitesh', 'k', 'IT', 50000, '2023-01-15'),
(2, 'Tahir', 'M', 'HR', 45000, '2022-05-20');