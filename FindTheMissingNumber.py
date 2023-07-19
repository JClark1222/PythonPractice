def missing_num(lst):
	numberList = {1,2,3,4,5,6,7,8,9,10}
	print(next(iter(numberList.difference(lst))))
	
missing_num([4,1,3,2,5,8,9,10,7])