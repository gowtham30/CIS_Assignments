select e.empid,e.emp_date, datediff(month, a.min_date, e.emp_date) as datedif FROM [TestDB].[dbo].[empid_date] e
inner join (SELECT [empid], min([emp_date]) as min_date
FROM [TestDB].[dbo].[empid_date] group by empid) a on a.empid = e.empid
