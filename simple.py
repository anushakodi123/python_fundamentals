# class Solution:
#     def maxProfit(self, prices) -> int:
#         max = 0
#         for i in range(len(prices)-1, 0, -1):
#             for j in range(i, -1, -1):
#                 diff = prices[i] - prices[j]
#                 if diff > max:
#                     max = diff
#         return max

# print(Solution().maxProfit([7,1,5,3,6,4]))

# class Solution:
#     def maxProfit(self, prices) -> int:
#         if not prices:
#             return 0

#         min_price = float('inf')
#         max_profit = 0

#         for price in prices:
#             if price < min_price:
#                 min_price = price
#                 print(min_price)
#             elif price - min_price > max_profit:
#                 max_profit = price - min_price

#         return max_profit

# print(Solution().maxProfit([7,6,4,3,1]))

# class Solution:
#     def twoSum(self, nums, target: int):
#         for i in range(0, len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 res = nums[i] + nums[j]
#                 print(res)
#                 if abs(res) == target:
#                     return [i, j]

# print(Solution().twoSum([2, 7, 11, 15], 9))


# class Solution:
#     def searchInsert(self, nums, target: int) -> int:
#         index = 0
#         if target in nums:
#             return nums.index(target)
#         for i in nums:
#             print(i > target)
#             if i > target:
#                 index = nums.index(i)
#                 break
#             else:
#                 index = len(nums)
#         return index


# print(Solution().searchInsert([1, 3, 5, 6], 2))

# class Solution:
#     def longestCommonPrefix(self, strs) -> str:
#         common = []
#         total_length = len(strs)
#         for i in range(0, len(strs)-1):
#             for j in range(i+1, len(strs)):
#                 new_str = ""
#                 string1 = strs[i]
#                 string2 = strs[j]
#                 length = min(len(string1), len(string2))
#                 for a in range(0, length):
#                     if string1[:a] == string2[:a]:
#                         new_str = new_str + string1[a]
#                 print(new_str)
#                 common.append(new_str)
#         return common

# print(Solution().longestCommonPrefix(["flower","flow","flight"]))

# class Solution:
#     def longestCommonPrefix(self, strs) -> str:
#         min_str = min(strs, key=len)
#         print(min_str)


# print(Solution().longestCommonPrefix(["flower","flow","flight"]))


# def roman_to_int(roman):
#     roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     prev_value = 0

#     for char in roman[::-1]:
#         print(char)
#         value = roman_numerals[char]
#         if value < prev_value:
#             result -= value
#         else:
#             result += value
#         prev_value = value

#     return result

# # Example usage
# roman_numeral = 'MCMLIV'
# print(f"The integer value of {roman_numeral} is: {roman_to_int(roman_numeral)}")


# def is_valid(s):
#     # Dictionary to hold matching pairs
#     bracket_map = {')': '(', '}': '{', ']': '['}
#     # Stack to hold opening brackets
#     stack = []
    
#     # Iterate through each character in the string
#     for char in s:
#         print("######", char)
#         # If the character is a closing bracket
#         if char in bracket_map:
#             # Pop the topmost element from the stack if it's not empty, otherwise use a dummy value
#             top_element = stack.pop() if stack else '#'
#             # Check if the top element matches the corresponding opening bracket
#             print(bracket_map[char])
#             if bracket_map[char] != top_element:
#                 return False
#         else:
#             # If it's an opening bracket, push it onto the stack
#             stack.append(char)
    
#     # If the stack is empty, all opening brackets were properly matched
#     return not stack

# # Example usage
# # s = "{[()()]}"
# # print(f"The string '{s}' is valid: {is_valid(s)}")

# s = "{[()]}"
# print(f"The string '{s}' is valid: {is_valid(s)}")



class Solution:
    def majorityElement(self, nums) -> int:
        length = len(nums)/2
        for i in nums:
            count = nums.count(i)
            if(count > length):
                return i
            
print(Solution().majorityElement([2,2,1,1,1,2,2]))
