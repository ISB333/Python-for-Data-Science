import sys

if len(sys.argv) != 2:
	print("AssertionError: more than one argument is provided")
	exit()

if sys.argv[1].lstrip('-').isdigit() is False:
	print("AssertionError: argument is not an integer")
else:
	if int(sys.argv[1]) % 2:
		print("Im Odd.")
	else:
		print("Im Even.")
