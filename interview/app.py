from collections import Counter
def word_freq(word):
	return Counter(word)

def count_anagrams(string, anagram):
	anagram_freq = word_freq(anagram)
	print(anagram_freq)
	count = 0
	for word in string.split(' '):
		word_freq_ = word_freq(word)
		print(word_freq_)
		if word_freq_ == anagram_freq:
			count += 1
	return count

def main():
	print(count_anagrams('A god is a godgod', 'dog'))

if __name__ == '__main__':
	main()