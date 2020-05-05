import random 
count = 0
def merge_sort(nums):
    def merge(nums, low, mid, high):
        left = [nums[i] for i in range(low, mid + 1)]
        right = [nums[i] for i in range(mid + 1, high + 1)]
        i = 0
        j = 0
        k = low
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


    def sort(nums, low, high):
        if low < high:
            mid = low + (high - low) // 2
            sort(nums, low, mid)
            sort(nums, mid + 1, high)
            i = low 
            j = mid + 1
            while i <= mid and j <= high :
                if nums[i] > nums[j]:
                    global count
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1 
            merge(nums, low, mid, high)

    sort(nums, 0, len(nums) - 1)

def main():
    nums = [random.randint(1,100) for _ in range(100)]
    print(nums)
    # nums = [1,3,2,3,1]
    print(nums)
    merge_sort(nums)
    print(nums == sorted(nums)) 
    print(count)

if __name__ == '__main__':
    main()
