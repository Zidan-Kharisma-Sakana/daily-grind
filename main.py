# dp = {}
# def f(n):
#   if n in dp:
#     return dp[n]
#   if n <= 3:
#     return n
#   res = f(n-1) + f(n-2) + f(n-3)
#   dp[n] = res
#   return res

# print('{:d}\n'.format(f(10)))
# print(dp)

# fibonacci but use last three instead of last two
def f(target):
    if target <= 3:
        return target
    accumulatorArray = [1, 2, 3] # holds last 3 curr 
    pointerAcc = 0 # idx of the element in accArray to be renewed
    curr = 4 # number that iterates to target
    while curr < target:
        # sum last 3, then renew/update the farther element (pointerAcc)
        currentSum = sum(accumulatorArray)
        accumulatorArray[pointerAcc] = currentSum
        # increment pointerAcc, but if exceed accArray length, back to 0 (rotating counter)
        pointerAcc = (pointerAcc + 1) % 3
        curr+=1
    # it stops on target -1, so we shall sum the last 3 curr
    return sum(accumulatorArray)

print(f(10))
    