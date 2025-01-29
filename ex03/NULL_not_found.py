import math

def NULL_not_found(object: any) -> int:
	result = type(object)
	if (object is None):
		print("Nothing:", object, result)
	elif (result == float):
		print("Cheese:", object, result)
	elif (result == int):
		print("Zero:", object, result)
	elif (result == str) and not object:
		print("Empty:", object, result)
	elif (result == bool) and not object:
		print("Fake:", object, result)
	else:
		print("Type not Found")
		return 1
	return 0
