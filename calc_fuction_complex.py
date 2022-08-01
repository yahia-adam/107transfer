#!/usr/bin/env python3
import tool

def calc_fuction_complex(av: [str], ac: int):
    frequency = 0
    result = 1
    nbr_function = 1
    while (frequency <= 1000):
        nbr_function = 1
        result = 1
        while (nbr_function != ac):
            num = av[nbr_function][::-1]
            denum = av[nbr_function + 1][::-1]
            num = num.split("*")
            denum = denum.split("*")
            for i in range (len(num)):
                num[i] = num[i][::-1]
            for i in range (len(denum)):
                denum[i] = denum[i][::-1]
            result = result * tool.div_betwen_num_and_denum_with_frequency(num, denum, frequency / 1000)
            nbr_function = nbr_function + 2
        print("{:.3f} ->"" {:.5f}" .format((frequency / 1000), result))
        frequency = frequency + 1
