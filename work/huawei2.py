
def special_add(a, b):

    result = 0
    if a == '!' and b == '!':
        result = 0
    elif a == '!' and b == '@' or a == '@' and b == '!':
        result = 13
    elif a == '!' and b == '#' or a == '#' and b == '!':
        result = 4
    elif a == '@' and b == '@':
        result = 7
    elif a == '@' and b == '#' or a == '#' and b == '@':
        result = 20
    elif a == '#' and b == '#':
        result = 5

    return result


n = int(input().strip())
num_str = input().strip()

add_index = num_str.find('+')
str_left = num_str[:add_index]
str_right = num_str[add_index+1:]
if '.' not in str_left:
    str_left = str_left + '.0'

if '.' not in str_right:
    str_right = str_right + '.0'


left_len1, left_len2 = len(str_left.split('.')[0]), len(str_left.split('.')[1])
right_len1, right_len2 = len(str_right.split('.')[0]), len(str_right.split('.')[1])
len1_max = max(left_len1, right_len1)
len2_max = max(left_len2, right_len2)

str_left = '0' * (len1_max - left_len1) + str_left
str_right = '0' * (len1_max - right_len1) + str_right

str_left = str_left + '0' * (len2_max - left_len2)
str_right = str_right + '0' * (len2_max - right_len2)
chars = ['@', '#', '!']
results = []
carry = 0   # 进位符
for i in range(len1_max+len2_max, -1, -1):

    if str_left[i] == '.':
        continue
    if str_left[i] in chars:
        result = special_add(str_left[i], str_right[i])
        carry = result // 10
        results.append(result % 10)
        continue
    result = int(str_left[i]) + int(str_right[i]) + carry
    carry = result // 10
    results.append(result % 10)

while carry:
    results.append(carry % 10)
    carry = carry // 10

results.reverse()
len_results = len(results)
final_result = 0
for i in range(len_results):
    final_result += results[i] * (10**(len_results-i-1))
final_result = final_result / 10**(len2_max)
print(final_result)






