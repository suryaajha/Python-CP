import sys
sys.path.insert(1, '../algo')

from stringi import search_rabinkarp

def main():
	txt = 'aaaaaaa'
	pat = 'aa'

	# txt = 'ABCXABCYABCXABCM'
	# pat = 'ABCXABCM'

	# print(search_bf(txt, pat))
	# print(search_rabinkarp(txt, pat))

	print(search_rabinkarp(txt, pat))

if __name__ == '__main__':
	main()