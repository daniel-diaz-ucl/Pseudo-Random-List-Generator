# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from src.stim_list import stimlist as stl


def create_list(test_data, col=1, k=1):
    f = open(test_data, "r")
    cc = csv.reader(f)
    next(cc)
    in_seq = []
    for row in cc:
        in_seq.append(row)

    my_list = stl.StimList(in_seq, col, k=k)

    my_list = my_list.prand_seq()

    return my_list


def check_seq(tested_list, col=1, k=1):
    """
    Correctness of an output sequence:
    tested_list: List[List]
    col: Int
    k: Int
    """
    for n_elem, o_elem in enumerate(tested_list):
        rep = n_elem - 1

        while n_elem - rep <= k and rep >= 0:

            if o_elem[col] != tested_list[rep][col]:
                break
            rep = rep - 1

        else:
            if rep < 0:
                continue

            return False

    return True


def test_output():
    col = 2
    k = 3
    test_list = create_list("test_data_0.csv", col, k)
    assert check_seq(test_list, col, k)

    col = 4
    k = 1
    test_list = create_list("test_data_1.csv", col, k)
    assert check_seq(test_list, col, k)

    col = 5
    k = 4
    test_list = create_list("test_data_2.csv", col, k)
    assert check_seq(test_list, col, k)
