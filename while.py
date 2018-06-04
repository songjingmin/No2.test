number = 23
while number:
	guess = int(input('enter an integer : '))
	if guess == number:
		print('ok, you guessen it.')
	elif guess < number:
		print('no, it is a little higher than that')
	else:
		print('no, it is a little lower than that')
else:
		print("the while loop is over")
		print('Done')