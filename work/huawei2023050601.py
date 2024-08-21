input_line1 = 14
input_line2 = [0xE77F]
from queue import PriorityQueue
# input_line1 = 18
# input_line2 = [0x677F, 0xFFFF]
n = input_line1
# n = int(input())
# input_line2 = input().strip().split()


status_ok = '0b'
for i in range(n):
    status_ok += '1'
status_ok = int(status_ok, 2)

holes = ''
for item in input_line2:
    tmp1 = bin(item)
    tmp2 = str(tmp1)[2:]
    tmp3 = '{:0>16s}'.format(tmp2)  # 位数不足时补0
    holes += tmp3
holes = holes[:n]
flag = False

move_right_max = holes.find('0') - holes.find('1')
if move_right_max > 0:
    for step in range(1, move_right_max+1):
        holes_move = bin(int('0b' + holes, 2) >> step)[2:]
        for i in range(n - len(holes_move)):
            holes_move = '0' + holes_move

        is_ok = (int('0b' + holes, 2) | int('0b' + holes_move, 2)) == status_ok
        if is_ok:
            flag = True
            holes_open = bin(int('0b' + holes, 2) ^ status_ok)[2:]
            for i in range(n - len(holes_open) - step):
                holes_open = '0' + holes_open
            for i in range(n - len(holes_open)):
                holes_open = holes_open + '0'
            print('+{}'.format(step))
            print(holes_open)
            break


move_left_max = holes[::-1].find('0') - holes[::-1].find('1')
if move_left_max > 0:
    for step in range(1, move_left_max+1):
        holes_move = bin(int('0b' + holes, 2) << step)[2:][-n:]

        is_ok = (int('0b' + holes, 2) | int('0b' + holes_move, 2)) == status_ok

        if is_ok:
            flag = True
            holes_open = bin(int('0b' + holes, 2) ^ status_ok)[2:]
            for i in range(n - len(holes_open) + step):
                holes_open = '0' + holes_open
            holes_open = holes_open[:n]
            print('-{}'.format(step))
            print(holes_open)
            break

if not flag: print(0)