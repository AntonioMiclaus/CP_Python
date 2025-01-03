for _ in range(int(input())):
	n = input()
	acount = n.count("A")
	bcount = n.count("B")
	if acount > bcount:
		print("A")
	else:
		print("B")