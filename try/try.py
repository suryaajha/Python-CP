def can_i(nums, start, k):
	print(start, k)
	if start == len(nums) and k == 0:
		return True
	if k < 0 or start == len(nums):
		return False 
	return can_i(nums, start + 1, k - nums[start]) or can_i(nums, start + 1, k)

def main():
	nums = [12, 1, 61, 5, 9, 2]
	print(can_i(nums, 0, 64))
if __name__ == '__main__':
	main()