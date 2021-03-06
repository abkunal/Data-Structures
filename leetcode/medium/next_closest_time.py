""" Next Closest Time - https://leetcode.com/problems/next-closest-time/description/

    Given a time represented in the format "HH:MM", form the next closest 
    time by reusing the current digits. There is no limit on how many 
    times a digit can be reused.

    You may assume the given input string is always valid. For example, 
    "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

    Example 1:

    Input: "19:34"
    Output: "19:39"
    
    Explanation: The next closest time choosing from digits 1, 9, 3, 4, 
    is 19:39, which occurs 5 minutes later.  It is not 19:33, because 
    this occurs 23 hours and 59 minutes later.
    
    Example 2:

    Input: "23:59"
    Output: "22:22"
    Explanation: The next closest time choosing from digits 2, 3, 5, 9, 
    is 22:22. It may be assumed that the returned time is next day's time 
    since it is smaller than the input time numerically.
"""

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour = int(time[:2])
        minutes = int(time[3:])

        nums = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]
        nums.sort()
        can = False
        n = None

        for i in nums:
            if i > int(time[-1]):
                can = True
                n = i
                break
        if can is True:
            return time[:-1] + str(n)

        for i in nums:
            if i > int(time[-2]) and int(str(i) + str(nums[0])) <= 59:
                can = True
                n = i
                break
        if can is True:
            return time[:-2] + str(n) + str(nums[0])

        for i in nums:
            if i > int(time[1]) and int(time[0] + str(i)) < 24:
                can = True
                n = i
                break
        if can is True:
            return time[0] + str(n) + ":" + str(nums[0])*2
        for i in nums:
            if i > int(time[0]) and int(str(i) + str(nums[0])) < 24:
                can = True
                n = i
                break
        if can is True:
            return str(n) + str(nums[0]) + ":" + str(nums[0]) + str(nums[0])
        return str(nums[0])*2 + ":" + str(nums[0])*2


a = Solution()
print(a.nextClosestTime("16:25"))