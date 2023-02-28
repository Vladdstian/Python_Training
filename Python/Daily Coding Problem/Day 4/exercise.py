nums = [3, 4, -1, 1]
nums2 = [1,2,0]

def check_lowest(nums_local):
    nums_local.sort()
    for num in nums_local:
        if num+1>0 and num+1 not in nums_local:
            return num+1
print(check_lowest(nums))
print(check_lowest(nums2))
