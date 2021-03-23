###password script
###password = a123456
###user can only have 3 times attempts
password = 'a123456'
n = 3 # maximum attempts
while True:
	pwd = input('Please enter your password.')
	if pwd == password:
		print('Welcome!')
		break
	else:
		n = n - 1
		print('Wrong password! You have', n,'attempts left!')
		if n == 0:
			break
