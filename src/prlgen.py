# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pseudo Random list generator from input file.
It creates offline input lists to feed psycholinguistics experiments
"""

import argparse
import csv
from stim_list import stimlist as stl

__author__ = "Daniel Diaz"
__copyright__ = "Daniel Diaz 2021"
__license__ = "GPL 3.0"
__version__ = "1.0.0"
__maintainer__ = "Daniel Diaz"
__email__ = "daniel.diaz@ucl.ac.uk"
__status__ = "Production"


def import_list(test_data):
    f = open(test_data, "r")
    cc = csv.reader(f)
    next(cc)
    in_seq = []
    for row in cc:
        in_seq.append(row)

    return in_seq


def write_list(output_list, list_num):
    for n in range(list_num):
        out_file = "output" "_" + str(n) + ".csv"
        f = open(out_file, "w", encoding='UTF8')
        cc = csv.writer(f)
        cc.writerows(output_list)


def create_random_list(new_list, col=1, trial=0, k=1):
    this_list = stl.StimList(new_list, col, trial, k=k)
    return this_list.prand_seq()


def main():
    # create parser object
    parser = argparse.ArgumentParser(description="Offline pseudoramdom list generator for psycholinguistic experiments")

    # defining arguments for parser
    parser.add_argument("-f", "--file", type=str, nargs=1,
                        metavar="file_name", default="input.csv",
                        help="Input file in CSV format.")

    parser.add_argument("-t", "--trial", type=int, nargs=1,
                        metavar="Number", default=0,
                        help="Trial ID column index. Default is 0")

    parser.add_argument("-c", "--cond", type=int, nargs=1,
                        metavar="Number", default=1,
                        help="Experimental Condition column index. Default is 1")

    parser.add_argument("-k", "--repetition", type=int, nargs=1,
                        metavar="Number", default=1,
                        help="Number of consecutive stimuli with the same condition. Default is 1")

    parser.add_argument("-o", "--outnum", type=int, nargs=1,
                        metavar="Number", default=1,
                        help="Number of list to be generated. Default is 1")

    # parse the arguments from standard input
    args = parser.parse_args()

    input_file = import_list(args.file[0])

    for file_num in range(args.outnum[0]):
        write_list(create_random_list(input_file,
                                      args.cond[0],
                                      args.trial[0],
                                      args.repetition[0]),
                   file_num)


if __name__ == "__main__":
    # calling the main function
    main()
