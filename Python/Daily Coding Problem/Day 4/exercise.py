nums = [3, 4, -1, 1]
nums2 = [1,2,0]

def check_lowest(nums):
    pos_numbers = [num if num >= 0 else 0 for num in nums]
    pos_numbers.sort()
    return [num+1 for num in pos_numbers if num+1 not in nums][0]

print(check_lowest(nums))
print(check_lowest(nums2))
