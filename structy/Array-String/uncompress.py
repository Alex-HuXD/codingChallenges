# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

# <number><char>

# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.


# 2 pointers

def uncompress(s):
    i,j = 0,0
    string = ''

    for char in s:
        if char in '0123456789':
            j += 1
        else:
            nums = int(s[i:j]) 
            letter = s[j]
            string += letter * nums
            j += 1
            i = j
    return string

print(uncompress('2c1a4z'))
