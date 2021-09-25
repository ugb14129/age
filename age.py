driving = input('Did you drive before? ')
if driving != 'Yes' and driving != 'No':
	print('Yes or No')
	
age = int(input('What is your age? '))
if driving == 'Yes' or 'yes':
	if age >= 18:
		print('Pass')
	else:
		print('Why did you drive the car before')	
elif driving == 'No':
	if age >= 18:
		print('You can get the DL')	
	else:
		print('You need to wait')	
else:
	print('Yes or No')		