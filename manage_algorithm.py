#!/usr/bin/env python3
import calc_fuction_complex
import calc_function_simple

def do_transfer(ac: int, av: [str]):
    if ac == 3:
        num = av[1][::-1]
        denum = av[2][::-1]
        num = num.split("*")
        denum = denum.split("*")
        for i in range (len(num)):
            num[i] = num[i][::-1]
        for i in range (len(denum)):
            denum[i] = denum[i][::-1]
        calc_function_simple.calc_fuction_simple(num , denum)
    if (ac > 3):
        calc_fuction_complex.calc_fuction_complex(av, ac)