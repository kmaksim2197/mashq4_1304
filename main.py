def solve(nums, target):
    d = {}
    for i, x in enumerate(nums):
        if target - x in d:
            return [d[target - x], i]
        d[x] = i

print(solve([2,7,11,15], 9))
