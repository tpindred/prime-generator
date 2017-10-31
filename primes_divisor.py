import math

def is_prime(number, prime_list):
	last_prime = math.ceil(math.sqrt(number))
	for i in prime_list:
		if i >= last_prime:
			return True
		if number % i == 0:
			return False

def get_primes(max_value):
	prime_list = [2]
	potential_primes = [n for n in range(3,max_value + 1) if n % 2 != 0]
	for n in potential_primes:
		if is_prime(n,prime_list) == True:
			prime_list.append(n)
	return prime_list
	
def main():
	while True:
		try:
			maximum = int(input('Enter the upper limit (must be >= 3):'))
			if maximum >= 3:
				break
			else:
				print('Please enter a number >= 3')
		except ValueError:
			print('Please enter a number.')
	primes = get_primes(maximum)
	print(primes)
		
main()