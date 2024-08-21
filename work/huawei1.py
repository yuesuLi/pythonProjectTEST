

n = int(input().strip())
seq = input().strip().split()
seq_len = len(seq)

all1 = '0b'
for _ in range(n):
    all1 += '1'
all1 = int(all1, 2)

holes = ''
for item in seq:

    tmp1 = bin(int(item, 16))
    tmp2 = str(tmp1)[2:]
    tmp3 = '{:0>16s}'.format(tmp2)  # 位数不足时补0
    holes += tmp3
holes = holes[:n]
flag = False

max_right = holes.find('0') - holes.find('1')
if max_right > 0:
    for step in range(1, max_right):
        holes_move = bin(int('0b' + holes, 2) >> step)[2:]
        for i in range(n - len(holes_move)):
            holes_move = '0' + holes_move
        is_ok = (int('0b' + holes, 2) | int('0b' + holes_move, 2)) == all1
        if is_ok:
            flag = True
            holes_open = bin(int('0b'+holes, 2) ^ all1)[2:]
            for _ in range(n-len(holes_open)-step):
                holes_open = '0' + holes_open
            for _ in range(n-len(holes_open)):
                holes_open = holes_open + '0'

            print('+{}'.format(step))
            print(holes_open)
            break



max_left = holes[::-1].find('0') - holes[::-1].find('1')
if max_left > 0:
    for step in range(1, max_left):
        holes_move = bin(int('0b' + holes, 2) << step)[2:]

        is_ok = (int('0b' + holes, 2) | int('0b' + holes_move, 2)) == all1
        if is_ok:
            flag = True
            holes_open = bin(int('0b'+holes, 2) ^ all1)[2:]

            for _ in range(n-len(holes_open) + step):
                holes_open = '0' + holes_open

            print('-{}'.format(step))
            print(holes_open)
            break
if not flag: print(0)