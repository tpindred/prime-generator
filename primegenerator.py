import math
import time

def get_primes(lowerlimit, upperlimit):

    potential_primes = [n for n in range(lowerlimit, upperlimit+1) if n % 2 != 0]
    primes = []

    for num in potential_primes:
        if num == 1:
            continue
        if num == 2:
            primes.append(num)
            continue
        lastdivisor = math.ceil(math.sqrt(num))
        divisors = [d for d in range(2, lastdivisor + 1)]
        if not any([d for d in divisors if num % d == 0]):
            primes.append(num)

    return primes

def main():
    print('''This script will evaluate all primes between the limits you specify.\n''')
    
    while True:
        try:
            lowerlimit = int(input('Enter the lower limit (must be >= 1):'))
            if lowerlimit >= 1:
                break
            else:
                print('Please enter a number >= 1.')
        except ValueError:
            print('Please enter a number.')

    while True:
        try:
            upperlimit = int(input('Enter the upper limit (must be >= lower limit + 2):'))
            if upperlimit >= lowerlimit + 2:
                break
            else:
                print('Please enter a number >= lower limit + 2.')
        except ValueError:
            print('Please enter a number.')
            
    start_time = time.time() 
    primes = get_primes(lowerlimit, upperlimit)
    print('\nThe primes between {} and {} are: {}'.format(lowerlimit, upperlimit, primes))
    print('Quantity of primes: {}'.format(len(primes)))
    print('{} seconds to complete.'.format(time.time()-start_time)) 

main()
