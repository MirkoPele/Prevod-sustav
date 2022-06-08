from time import sleep
from tomlkit import boolean
import re

# input number base from and to which we want to convert number
def input_base(fr: boolean):
    base = 0
    while True:
        try:
            if fr:
                base = int(input("Enter the number base, from which you want to convert number: "))
            else:
                base = int(input("Enter the number base, into which you want to convert number: "))
        except:
            print("Base must be an integer!")
            continue
        if base in range(2, 17):
            break
        print("Input is not in right range!")
    return base

# input number which we want to convert
def input_number():
    pattern = re.compile('^[0123456789ABCDEF]+$')
    num = ""
    while True:
        num = input("Enter the number to be converted: ").upper().strip()
        if not re.search(pattern, num):
            print("Your input probbably contains wrong characters!")
            continue
        break
    return num

# convert number in string format to decimal base number
def convert_to_decimal(base_from: int, num: str):
    hex_values = {"A": 10, "B":11, "C":12, "D":13, "E":14, "F":15}
    summary = 0
    for idx, digit in enumerate(num[::-1]):
        if not digit.isdigit():
            summary += hex_values[digit] * (base_from ** idx)
        else:
            summary += int(digit) * (base_from ** idx)
    return summary


def convert(base_from: int, base_to: int, num: str):
    hex_values = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    num_in_dec = convert_to_decimal(base_from, num)
    rest = 0
    result_str = ""
    while num_in_dec != 0:
        rest = num_in_dec % base_to
        num_in_dec //= base_to
        if rest > 9:
            result_str += hex_values[rest]
        else:
            result_str += str(rest)
    return result_str[::-1]

from_base = input_base(True)
to_base = input_base(False)
number = input_number()
result = convert(from_base, to_base, number)
print(f"Converted number is: {result}.")
sleep(5) # wait 5 seconds before closing program