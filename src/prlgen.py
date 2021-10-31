# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pseudo Random list generator from input file.
For offline input lists to feed psycholinguistics experiments
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


def create_random_list(new_list, col=1, k=1):
    this_list = stl.StimList(new_list, col, k=k)
    return this_list.prand_seq()


def main():
    parser = argparse.ArgumentParser(description="Offline pseudoramdom list generator for psycholinguistic experiments")

    # parse the arguments from standard input
    args = parser.parse_args()
    

if __name__ == "__main__":
    # calling the main function
    main()
