def special_add(a, b):
    """处理特殊符号的加法运算"""
    if a == '!' and b == '!':
        return '0'
    elif a == '!' and b == '@' or a == '@' and b == '!':
        return '13'
    elif a == '!' and b == '#' or a == '#' and b == '!':
        return '4'
    elif a == '@' and b == '@':
        return '7'
    elif a == '@' and b == '#' or a == '#' and b == '@':
        return '20'
    elif a == '#' and b == '#':
        return '5'


def calculate(expression):
    """计算表达式的值"""
    # 找到加号的位置
    operator_index = expression.index('+')
    # 获取左边的操作数
    left_operand = expression[:operator_index]
    # 获取右边的操作数
    right_operand = expression[operator_index + 1:]
    if '.' not in left_operand:
        left_operand = left_operand + '.0'
    if '.' not in right_operand:
        right_operand = right_operand + '.0'

    max_digits = max(len(left_operand.split(".")[-1]), len(right_operand.split(".")[-1]))

    # 将两个数小数点后面的位数补齐
    if len(left_operand.split(".")[-1]) != max_digits:
        left_operand = left_operand + '0' * (max_digits - len(left_operand.split(".")[-1]))
    if len(right_operand.split(".")[-1]) != max_digits:
        right_operand = right_operand + '0' * (max_digits - len(right_operand.split(".")[-1]))

    left_operand = left_operand.split('.')[0] + left_operand.split('.')[1]
    right_operand = right_operand.split('.')[0] + right_operand.split('.')[1]

    # 判断是否有特殊符号
    if set(left_operand) & {'!', '@', '#'} or set(right_operand) & {'!', '@', '#'}:
        carry = 0  # 进位值
        if len(left_operand) < len(right_operand):
            left_operand = '0' * (len(right_operand) - len(left_operand)) + left_operand
        elif len(left_operand) > len(right_operand):
            right_operand = '0' * (len(left_operand) - len(right_operand)) + right_operand
        res_list = []  # 结果数组
        for i in range(len(left_operand) - 1, -1, -1):
            if left_operand[i] in {'!', '@', '#'} and right_operand[i] in {'!', '@', '#'}:
                res = special_add(left_operand[i], right_operand[i])
                res_list.append(str((int(res) + carry) % 10))
                carry = (int(res) + carry) // 10
            else:
                # print(left_operand[i], right_operand[i])
                temp = int(left_operand[i]) + int(right_operand[i]) + carry
                res_list.append(str(temp % 10))
                carry = temp // 10
        # 处理剩余的进位
        while carry > 0:
            res_list.append(str(carry % 10))
            carry //= 10
        # 反转结果
        res_list.reverse()
        # 拼接成字符串
        res_str = ''.join(res_list)
        res = eval(res_str) / 10 ** max_digits
    else:
        res = (eval(left_operand) + eval(right_operand)) / 10 ** max_digits
    # 计算表达式的值
    return res


# 获取输入
n = int(input())
expression = input().strip()

# 计算表达式并输出结果
print(calculate(expression))
