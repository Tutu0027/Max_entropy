# -*- coding: utf-8 -*-
#!/usr/bin/env python
#两数之和
def twoSum(nums, target):
    ll = []
    i = 0
    while i < len(nums):
        diff = target-nums[i]
        if diff < 0:
            i +=1
            continue
        for j in range(i + 1, len(nums)):
            if nums[j] == diff:
                ll.append(i)
                ll.append(j)
                return ll
        i += 1
ll = twoSum([2,11,7,8],9)
print(ll)