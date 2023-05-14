from TestData import TestData

JobsMaxAverageMin = TestData('SELECT TOP (1) {} FROM {} WHERE {} = (SELECT MAX({}) FROM {}) '
                             'UNION ALL '
                             'SELECT {} FROM {} '
                             'UNION ALL '
                             'SELECT TOP (1) {} FROM {} WHERE {} = (SELECT MIN({}) FROM {}) ',
                             ['\'Max\' as Metric, job_title as Title, max_salary as Salary',
                              'hr.jobs', 'max_salary', 'max_salary', 'hr.jobs',
                              '\'Average\' as Metric, NULL, AVG(Salary) as Salary', 'hr.employees',
                              '\'Min\' as Metric, job_title as Title, min_salary as Salary',
                              'hr.jobs', 'min_salary', 'min_salary', 'hr.jobs'], [['Max', 'President', 40000.0],
                                                                                  ['Average', None, 8060.0],
                                                                                  ['Min', 'Stock Clerk', 2000.0]])

JobsEmployeesCount = TestData('SELECT {} FROM {} JOIN {} ON {} = {} GROUP BY {} ORDER BY {} DESC',
                              ['Jobs.job_id AS ID, Jobs.job_title AS Title, COUNT(*) AS PositionTotalCount',
                               'hr.jobs as Jobs', 'hr.employees as Employees', 'Jobs.job_id', 'Employees.job_id',
                               'Jobs.job_id, Jobs.job_title', 'PositionTotalCount'],
                              [[9, 'Programmer', 5],
                               [6, 'Accountant', 5],
                               [13, 'Purchasing Clerk', 5],
                               [16, 'Sales Representative', 4],
                               [19, 'Stock Manager', 4],
                               [17, 'Shipping Clerk', 2],
                               [5, 'Administration Vice President', 2],
                               [15, 'Sales Manager', 2],
                               [18, 'Stock Clerk', 1],
                               [14, 'Purchasing Manager', 1],
                               [7, 'Finance Manager', 1],
                               [8, 'Human Resources Representative', 1],
                               [10, 'Marketing Manager', 1],
                               [11, 'Marketing Representative', 1],
                               [12, 'Public Relations Representative', 1],
                               [1, 'Public Accountant', 1],
                               [2, 'Accounting Manager', 1],
                               [3, 'Administration Assistant', 1],
                               [4, 'President', 1]])

