nums = [-1,-100,3,99]
k = 2
k = k % len(nums)
nums[:] = nums[-k:] + nums[:-k]
print(nums) #for see result
