class BitVector:

	def __init__(self, bitvector = 0):
		self.bitvector = bitvector

	def get(self, bit_n):
		return 1 if (self.bitvector & (1 << bit_n)) > 0 else 0

	def set(self, bit_n):
		self.bitvector = self.bitvector | (1 << bit_n)

	def unset(self, bit_n):
		self.bitvector = self.bitvector & ~(1 << bit_n)

	def __repr__(self):
		return bin(self.bitvector)

	def value(self):
		return self.bitvector

def main():

	n = [1,2,3]

	t = ((x, i) for i, x in enumerate(n))

	print((t))

	bv = BitVector()
	bv.set(1)
	bv.set(0)
	bv.unset(0)

	print(bv.get(0))

	print(bv)

if __name__ == '__main__':
	main()