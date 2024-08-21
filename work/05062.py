def special_add(a, b):
    """处理特殊符号的加法运算"""
    special = {'!': {'!': 0, '@': 13, '#': 4},
               '@': {'@': 7, '#': 20},
               '#': {'#': 5}}
    return str(special[a][b]) if a in special and b in special[a] else None


def calculate(expression):
    """计算表达式的值"""
    # 找到加号的位置
    operator_index = expression.index('+')
    # 获取左边的操作数
    left_operand = expression[:operator_index]
    # 获取右边的操作数
    right_operand = expression[operator_index + 1:]
    if '.' not in left_operand:
        left_operand += '.0'
    if '.' not in right_operand:
        right_operand += '.0'

    max_digits = max(len(left_operand.split(".")[-1]), len(right_operand.split(".")[-1]))

    # 将两个数小数点后面的位数补齐
    left_operand = left_operand.replace('.', '').rjust(max_digits, '0')
    right_operand = right_operand.replace('.', '').rjust(max_digits, '0')

    # 判断是否有特殊符号
    if any(c in left_operand+right_operand for c in ['!', '@', '#']):
        carry = 0  # 进位值
        res_list = []  # 结果数组
        for i in range(len(left_operand) - 1, -1, -1):
            res = special_add(left_operand[i], right_operand[i])
            if res is not None:
                res_list.append(str((int(res) + carry) % 10))
                carry = (int(res) + carry) // 10
            else:
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