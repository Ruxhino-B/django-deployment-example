# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i] == 1 and nums[i+1] == 2 and nums [i+2] ==3:
#             return True
#     return False
#
# arrayCheck([1,1,2,2,3,3,1,2,3])

# def string_bits(str):
#     print(str[::2])
#
# b = string_bits('Heeololeo')
# print(b)
def string_bits(str):
    result = ''
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result
