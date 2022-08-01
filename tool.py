#!/usr/bin/env python3

def cal_function_x(function: [str], x: int)->int:
    result = float(function[0])
    count = 1
    len_function = len(function)
    while count != len_function:
        result = float(function[count]) + x * result
        count = count + 1
    return (result)


def div_betwen_num_and_denum_with_frequency(num: [str], denum: [str], frequency :float):
    result = 0
    num_x = cal_function_x(num, frequency)
    denum_x = cal_function_x(denum, frequency)
    if (denum_x != 0):
        result = (num_x / denum_x)
    else :
        result = 0
    return (result)
