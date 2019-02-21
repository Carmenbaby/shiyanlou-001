#!/usr/bin/env python3

import sys

def calculator(salary_sum):
    x = int(salary_sum - 0 - 0 - 5000)
    
    if x <= 3000:
        sum = float(x * 0.03)
    elif x > 3000 and x < 12000:
        sum = float(x * 0.10 -210)
    elif x > 12000 and x < 25000:
        sum = float(x * 0.20 - 1410)
    elif x > 25000 and x < 35000:
        sum = float(x * 0.25 - 2660)
    elif x > 35000 and x < 55000:
        sum = float(x * 0.30 - 4410)
    elif x > 55000 and x < 80000:
        sum = float(x * 0.30 - 7160)
    else:
        sum = float(x * 0.45 - 15160)
    print('{:.2f}'.format(sum))

if __name__ == '__main__':

    try:
        salary_sum = int(sys.argv[1])
    except:
        print('Parameter Error')
    calculator(salary_sum)
