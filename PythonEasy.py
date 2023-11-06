def str_to_list( str ) :
	new_list = []
	for e in str:
		# if string is empty space
		if e == ' ':
			continue
		# check if is digit
		elif e.isdigit():
			if int(e) > 5:
				continue
		# append if passed all tests
		new_list.append(e)

	return new_list