SELECT  *
	FROM [TestDB].[dbo].[Table_A] a
	left JOIN [TestDB].[dbo].[Table_B] b
	ON a.TableA = b.TableB 