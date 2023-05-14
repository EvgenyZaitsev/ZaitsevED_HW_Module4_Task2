from datetime import date
from TestData import TestData

EmployeesCount = TestData('SELECT {} FROM {} ', ['COUNT(*) AS TotalCount', 'hr.employees'], [[40]])

EmployeesOldestOne = TestData('SELECT TOP(1) {} FROM {} WHERE {} = (SELECT MIN({}) FROM {})',
                              ['employee_id as ID, first_name as FirstName, last_name as LastName, '
                               'hire_date as HireDate, salary as Salary',
                               'hr.employees', 'hire_date', 'hire_date', 'hr.employees'],
                              [[100, 'Steven', 'King', date(1987, 6, 17), 24000.0]])
