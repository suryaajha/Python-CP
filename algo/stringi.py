'''
	Time Complexity = O(m*(n - m)) ==> O(n*m)
	Space Complexity = O(1) if need to return first found starting index 
					   O(n) if need to return all found starting index
'''
def search_bf(txt, pat):

	n = len(txt)
	m = len(pat)

	output = []
	# Consider every char as starting char
	for i in range(n - m + 1):
		for j in range(m):
			if txt[i + j] != pat[j]:
				break 
		if j == m - 1: # if whole pat is overseved without break means we found pat as substring
			# output.append(txt[i: i + m]) # if need to return the substring that was matched debugging
			# OR
			output.append(i) # i is the start of such substring

	return output

def search_rabinkarp(txt, pat):
	n = len(txt)
	m = len(pat)

	output = []

	base = 26 # Considering all ascii values
	prime = 1234567891 # Large Prime number for modding

	pat_hash = 0
	txt_hash = 0

	# Compute the Hash Value for pattern
	'''
	Pat 	= ABC
	Hash 	= (A*base^m-1 + .... + C*base^0) % prime
	HASH 	= (65*base^2 + 66*base^1 + 67*base^0) % prime
			= 65*base^2 % prime + 66*base^1 % prime + 67*base^0 % prime
	'''
	for i in range(m):
		pat_hash += ord(pat[i]) * (base ** (m - 1 - i))

	# Similarly compute the Hash Value for txt
	for i in range(m):
		txt_hash += ord(txt[i]) * (base ** (m - 1 - i))

	for i in range(n - m + 1):
		if pat_hash == txt_hash: # If hash are same then 2 strings can be equal but need to check mannually

			# Mannually check if 2 strings are same one char by one char
			for j in range(m):
				if txt[i + j] != pat[j]:
					break

			# if all chars were compared of pattern then they were really equal
			if j == m - 1:
				output.append(i)
		
		# Irrespective of the fact whether the choosen start 'i' got a subtring match or not
		# Do a roll hash of txt

		'''
		S[i:m] = 'ABC'
		S[i:m+1] = 'ABCD'
		txt_hash = (65*base^2 + 66*base^1 + 67*base^0) % prime
		txt_hash = txt_hash - 65*base^2
		txt_hash = 66*base^1 + 67*base^0
		txt_hash = (66*base^1 + 67*base^0) * base
		txt_hash = 66*base^2 + 67*base^1
		txt_hash = (66*base^1 + 67*base^0 + D) % prime
		'''
		if i != n - m: # dont include when we cant go further 
			txt_hash = (txt_hash - (ord(txt[i]) * (base ** (m - 1)))) * base + ord(txt[i + m]) % prime 

	return output

'''
	LPS = []
	LPS[i] => Length of longest prefix which is also suffix
'''

def search_kmp(txt, pat):

	def construct_lps(pat, m):
		lps = [0] * m

		longest_prefix_suffix_till_now = 0
		lps[0] = 0

		i = 1 
		while i < m: # construct lps 1..m-1
			if pat[i] == pat[longest_prefix_suffix_till_now]:
				longest_prefix_suffix_till_now += 1
				lps[i] = longest_prefix_suffix_till_now
				i += 1
			else:
				if longest_prefix_suffix_till_now == 0:
					lps[i] = 0
					i += 1
				else:
					longest_prefix_suffix_till_now = lps[longest_prefix_suffix_till_now - 1]

		return lps

	n = len(txt)
	m = len(pat)

	output = []

	lps = construct_lps(pat, m)
	print(lps)

	txt_ptr = 0
	pat_ptr = 0

	while txt_ptr < n:
		if txt[txt_ptr] == pat[pat_ptr]:
			pat_ptr += 1
			txt_ptr += 1

		if pat_ptr == m:
			output.append(txt_ptr - m) # Store starting index of pattern in txt
			pat_ptr = lps[pat_ptr - 1]

		elif txt_ptr < n and pat[pat_ptr] != txt[txt_ptr]:
			if pat_ptr == 0: # If mismatch happens at first character
				txt_ptr += 1  # Start 
			else: # Mismatch happend at j 
				# Shift the pattern by lps[txt_ptr] and since the longest suffix will be prefix 
				# there is no need to match those letters 
				# instead start matching from lps[j - 1]
				pat_ptr = lps[pat_ptr - 1] 
	return output


def main():
	txt = 'aaaaaaa'
	pat = 'aa'

	# txt = 'ABCXABCYABCXABCM'
	# pat = 'ABCXABCM'

	# print(search_bf(txt, pat))
	# print(search_rabinkarp(txt, pat))

	print(search_kmp(txt, pat))

if __name__ == '__main__':
	main()