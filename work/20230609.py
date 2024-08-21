import re

mystr = '12B13D11A11A12A'

numbers = re.findall(r'\d+', mystr)
nums = set(numbers)
mysum = 0

for number in numbers:
    mysum += int(number)
print(mysum)