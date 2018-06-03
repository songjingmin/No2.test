number = 23
guess = int(input('enter a integer : '))
if guess == number: # 注意：这里是 == 不是=
	print('ok, you guessed it.')
	print("but you do not win any prize!")
elif guess < number:
	print('no, it is a little higher than that')
else:
	print('no, it is a little lower than that')
	print('Done')