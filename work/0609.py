input_str = 'AC1CF12D12BAS15CC'


def is_char(s):
    if ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z'):
        return True
    else:
        return False


l_i = r_i = 0
nums = []
while r_i < len(input_str):
    if is_char(input_str[r_i]):
        if r_i - l_i > 0:
            nums.append(int(input_str[l_i:r_i]))
        r_i += 1
        l_i = r_i
    else:
        r_i += 1
if r_i - l_i > 0:
    nums.append(int(input_str[l_i:r_i]))

nums = set(nums)
sum = 0
for item in nums:
    sum += item
print(sum)
