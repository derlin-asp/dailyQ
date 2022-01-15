
def twoSumsBooleanFast():
    #cannnot use position

    nums = [1,2,3,4,5,6,7,8,9]
    k = 22
    nums = [1,7,2,4,5,6,3,8,9]
    k = 17
    my_dict = {}
    # time complexly = n
    # space = N^2
    for x in range(len(nums)):
        my_dict[nums[x]] = True
        diff = k - x
        if diff in my_dict:
            return True

    return False

def twoSumsBooleanBrute():
    #cannnot use position
    #time complexly = n^2
    #space = N
    nums = [1,2,3,4,5,6,7,8,9]
    k = 22
    nums = [1,7,2,4,5,6,3,8,9]
    k = 2
    if len(nums) == 0:
        return

    for x in range(len(nums)):
        for y in range(len(nums)):
            if x != y and nums[x] + nums[y] == k:
                return True
    return False



assert twoSumsBooleanFast()
