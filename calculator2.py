#!/usr/bin/env python3

import sys

output_dict = {}

def calculator(value):
    sum = 0.00
    socity = float(value * 0.165)
    if value <= 5000:
        sum = value - socity
    else:
        temp = (value - 5000 - socity)
        if temp <= 3000:
            sum = value -socity - temp * 0.03
        elif temp > 3000 and temp <= 12000:
            sum = value -socity - temp * 0.10 + 210
        elif temp > 12000 and temp <= 25000:
            sum=value -socity - temp * 0.20 +210+1410
        elif temp > 25000 and temp <= 35000:
            sum=value -socity - temp * 0.25+210+1410+2660
        elif temp> 35000 and temp <= 55000:
            sum=value -socity - temp * 0.30+210+1410+2660+4410
        elif temp> 55000 and temp <= 80000:
            sum=value -socity - temp * 0.35+210+1410+2660+4410+7160
        else:
            sum=value -socity - temp * 0.45+210+1410+2660+4410+7160+15160
    return sum

def hanle_data(arg):
    if arg.count(':') != 1:
        print('Parameter Error')
        return

    key,value = arg.split(':')
    try:
        key = int(key)
        value = int(value)
    except:
        print('Parameter Error')
        return 
    output_dict[key] = calculator(value)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Parameter Error')

    for arg in sys.argv[1:]:
        hanle_data(arg)

    for key,value in output_dict.items():
        print('{}:{:.2f}'.format(key,value))
