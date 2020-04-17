# Generate all primes 2, 3, 5 ..... n
# such that n <= limit
def generate_primes_brute_force(limit):
	primes = []
	primes.append(2)

	for k in range(3, limit):
		for prime in primes:
			if k % prime == 0:
				break
		else:
			primes.append(k)
	return primes
	
def generate_primes_sieve(limit):
	limit += 1
	memo = [True] * limit
	i = 2
	while i * i <= limit: # while i <= sqrt(n)
		# If visiting i first time then it must be prime
		if memo[i]:
			# Set all the multiples of i to False, since they cannot be prime anymore
			# Start at i ^ 2 since all the values less than i^2 will be already marked Just for optimization
			for j in range(i * i, limit, i):
				memo[j] = False
			# increment i to get new value
		i += 1
	primes = []
	for i in range(2, limit):
		if memo[i]:
			primes.append(i)

	return primes


def main():
	l = 100
	# p = generate_primes_brute_force(l)
	q = generate_primes_sieve(l)

	print(q)

if __name__ == '__main__':
	main()