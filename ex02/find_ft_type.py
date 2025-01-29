def all_thing_is_obj(object:any) -> int:
	result = type(object)
	if result == list:
		print("List :", type(object))
	elif result == tuple:
		print("Tuple :", type(object))
	elif result == set:
		print("Set :", type(object))
	elif result == dict:
		print("Dict :", type(object))
	elif result == str:
		print(object, "is in the kitchen :", type(object))
	else:
		print("Type not found")
	return 42
