'''
nums = [2,7,11,15]
target = 9
[0, 1]

nums = [3,2,4]
target = 6
[1,2]

nums = [3,3]
target = 6
[0,1]
'''

def twoSum( nums, target):
    ind = []
    for item in range(len(nums)):
        if target != 0:
                for item2 in range(len(nums)):
                    if item != item2:
                        if nums[item] == nums[item2]:
                            if nums[item] + nums[item2] == target:
                                ind.append(item)
                                ind.append(item2)
                                return ind
                            
                        if nums[item] + nums[item2] == target:
                            ind.append(item)
                            ind.append(item2)
                            return ind
        else:
            for item2 in range(len(nums)):
                if item != item2:    
                    if nums[item] + nums[item2] == target:
                            ind.append(item)
                            ind.append(item2)
                            return ind
            
                            
                       
    

nums = [3,3]
target = 6
print(twoSum(nums,target))