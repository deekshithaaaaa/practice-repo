def pairs_with_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] +nums[j]== target:
                print((nums[i],nums[j]))
            
    return None
print(pairs_with_sum( nums = [1, 2, 3, 4, 5], target = 6))
