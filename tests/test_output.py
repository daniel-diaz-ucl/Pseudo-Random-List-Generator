# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import src.stim_list as stl


def create_list():
    f = open("test_data.csv", "r")
    cc = csv.reader(f)
    next(cc)
    in_seq = []
    for row in cc:
        in_seq.append(row)

    my_list = stl.StimList(in_seq, 2, k=3)

    my_list = my_list.prand_seq()

    return my_list


def column(matrix, i):
    return [row[i] for row in matrix]


def test_output():
    test_list = create_list()
    print(test_list)

    test_column = column(test_list, 2)
    print(test_column)

    assert test_column == ['Blue', 'Blue', 'Blue', 'Red', 'Blue', 'Blue', 'Blue', 'Red', 'Blue', 'Blue', 'Blue', 'Red', 'Blue', 'Blue', 'Blue', 'Red', 'Blue', 'Blue', 'Blue', 'Red', 'Blue', 'Blue', 'Blue']
