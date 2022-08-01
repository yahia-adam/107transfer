#!/usr/bin/env python3
import tool

def calc_fuction_simple(num: [str], denum: [str]):
    frequency = 0
    num_x = 0
    denum_x = 0
    num_x = 0

    while frequency <= 1000:
        result = tool.div_betwen_num_and_denum_with_frequency(num, denum, frequency / 1000)
        print("{:.3f} ->"" {:.5f}" .format((frequency / 1000), result))
        frequency = frequency + 1
