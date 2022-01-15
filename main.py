#Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?
#
# Upgrade to premium and get in-depth solutions to every problem, including this one.
#
# If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!
#
# Master algorithms together on Binary Search. Create a room, invite your friends, and race to finish the problem!


def twoSumsBooleanFast():
    #cannnot use position

    nums = [1,2,3,4,5,6,7,8,9]
    k = 22
    nums = [1,7,2,4,5,6,3,8,9]
    k = 17
    my_dict = {}
    # time complexly = n
    # space = 2N = n
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
        return False

    for x in range(len(nums)):
        for y in range(len(nums)):
            if x != y and nums[x] + nums[y] == k:
                return True
    return False



assert twoSumsBooleanFast()
