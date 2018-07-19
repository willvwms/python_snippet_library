except Exception as err: 

	print("============================================")
	print("Skipped: " + i)
	print("Error:")
	print("line: " + str(sys.exc_info()[-1].tb_lineno) )
	print(err)
	print("============================================")
