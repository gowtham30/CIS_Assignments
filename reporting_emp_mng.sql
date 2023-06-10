SELECT [emp_id]
  FROM [TestDB].[dbo].[emp_mng]
  where mang_id in (SELECT [emp_id]
  FROM [TestDB].[dbo].[emp_mng]
  where mang_id in (SELECT [emp_id]
  FROM [TestDB].[dbo].[emp_mng]
  where mang_id = '1')) and emp_id != 1