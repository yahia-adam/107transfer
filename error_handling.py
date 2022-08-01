#!/usr/bin/env python3

def correct_arguments(ac: int, av: [str])-> int:
    j: int = 0
    i: int = 1
    len_str: int = 0
    while (i != ac):
        j = 0
        len_str = len(av[i])
        while (j != len_str):
            if (av[i][j] != '*' and av[i][j] != '-') and (av[i][j] > '9' or av[i][j] < '0'):
                return (-1)
            j = j + 1
        i = i + 1
    return (0)

def error(ac : int, av : [str]) -> int:
    if (ac % 2 == 0 or ac < 3):
        return (-1)
    if correct_arguments(ac, av) == -1:
        return (-1)
    return (0)
