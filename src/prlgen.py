# !/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import sys

from stim_list import stimlist as stl

"""
This script generates pseudo-random lists from an input file in CSV format. It is intended for use in creating offline input lists for psycholinguistic experiments.

The script accepts several command-line arguments that allow the user to specify the input file, the number of output lists to generate, and various parameters that control the generation of the pseudo-random lists. The generated lists are written to output files in CSV format.

The script uses the `stim_list` module to generate the pseudo-random lists. This module implements a custom algorithm for generating pseudo-random sequences based on the input data and the specified parameters.
"""

__author__ = "Daniel Diaz"
__copyright__ = "Daniel Diaz 2021"
__license__ = "GPL 3.0"
__version__ = "1.1.0"
__maintainer__ = "Daniel Diaz"
__email__ = "daniel.diaz@ucl.ac.uk"
__status__ = "Production"


def import_list(test_data):
    """
    Reads data from a CSV file and returns it as a list of lists.

    :param test_data: The path to the CSV file.
    :return: A list of lists containing the data from the CSV file.
    """
    f = open(test_data, "r")
    cc = csv.reader(f)
    next(cc)
    in_seq = []
    for row in cc:
        in_seq.append(row)

    return in_seq


def write_list(output_list, list_num, base_name):
    """
    Writes the given output list to a CSV file.

    :param output_list: The list of data to write to the CSV file.
    :param list_num: The number of the output file.
    :param base_name: The base name for the output file.
    """
    out_file = base_name + "_" + str(list_num) + ".csv"
    f = open(out_file, "w", encoding="UTF8")
    cc = csv.writer(f)
    cc.writerows(output_list)


def create_random_list(new_list, col=1, trial=0, k=1):
    """
    Creates a pseudo-random sequence from the given input list.

    :param new_list: The input list of data.
    :param col: The index of the column containing the experimental condition.
    :param trial: The index of the column containing the trial ID.
    :param k: The number of consecutive stimuli with the same condition.
    :return: A pseudo-random sequence generated from the input list.
    """
    this_list = stl.StimList(new_list, col, trial, k=k)
    return this_list.prand_seq()


def main():
    """
    Parses command-line arguments and generates pseudo-random lists based on the provided input file.

    The function accepts the following command-line arguments:

    -f, --file: The path to the input file in CSV format. Default is "input.csv".
    -t, --trial: The index of the column containing the trial ID. Default is 0.
    -c, --cond: The index of the column containing the experimental condition. Default is 1.
    -k, --repetition: The number of consecutive stimuli with the same condition. Default is 1.
    -n, --name: The base name for output files. Default is "output".
    -o, --outnum: The number of lists to be generated. Default is 1.

    The function reads data from the input file, generates the specified number of pseudo-random lists using the `create_random_list` function, and writes each list to a separate output file using the `write_list` function.
    """
    # create parser object
    parser = argparse.ArgumentParser(
        description="Offline pseudoramdom list generator for psycholinguistic experiments"
    )

    # defining arguments for parser
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        nargs=1,
        metavar="file_name",
        default=["input.csv"],
        help="Input file in CSV format.",
    )

    parser.add_argument(
        "-t",
        "--trial",
        type=int,
        nargs=1,
        metavar="Number",
        default=[0],
        help="Trial ID column index. Default is 0",
    )

    parser.add_argument(
        "-c",
        "--cond",
        type=int,
        nargs=1,
        metavar="Number",
        default=[1],
        help="Experimental Condition column index. Default is 1",
    )

    parser.add_argument(
        "-k",
        "--repetition",
        type=int,
        nargs=1,
        metavar="Number",
        default=[1],
        help="Number of consecutive stimuli with the same condition. Default is 1",
    )

    parser.add_argument(
        "-n",
        "--name",
        type=str,
        nargs=1,
        metavar="file_name",
        default=["output"],
        help="Base name for output files.",
    )

    parser.add_argument(
        "-o",
        "--outnum",
        type=int,
        nargs=1,
        metavar="Number",
        default=[1],
        help="Number of list to be generated. Default is 1",
    )

    # parse the arguments from standard input
    args = parser.parse_args()

    # check if any arguments were provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    input_file = import_list(args.file[0])

    for file_num in range(args.outnum[0]):
        write_list(
            create_random_list(
                input_file, args.cond[0], args.trial[0], args.repetition[0]
            ),
            file_num + 1,
            args.name[0],
        )


if __name__ == "__main__":
    # calling the main function
    main()
