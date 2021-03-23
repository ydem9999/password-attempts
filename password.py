###password script
###password = a123456
###user can only have 3 times attempts
password = 'a123456'
n = 3 # maximum attempts
while n > 0:
	n = n - 1
	pwd = input('Please enter your password.')
	if pwd == password:
		print('Welcome!')
		break
	else:
		print('Wrong password!')
		if n > 0:
			print('You have', n,'attempts left!')
		else:
			print('No more attempts！')
		
