import random


def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums


def quick_sort(nums):
    comp = 0
    if len(nums) > 1:
        x = nums[random.randint(0, len(nums)-1)]
        low = [i for i in nums if i < x]
        eq = [i for i in nums if i == x]
        hi = [i for i in nums if i > x]
        nums = quick_sort(low) + eq + quick_sort(hi)
    return nums


nums = [i for i in range(100)]
nums.reverse()
print(quick_sort(nums))
