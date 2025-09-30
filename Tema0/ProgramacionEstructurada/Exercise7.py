
userNumber = int(input("Enter number: "))

if userNumber <= 1:
	print("Is not a prime number.")
else:
	is_prime = True
	for i in range(2, int(userNumber ** 0.5) + 1):
		if userNumber % i == 0:
			is_prime = False
			break
	if is_prime:
		print("Is a prime number.")
	else:
		print("Is not a prime number.")

