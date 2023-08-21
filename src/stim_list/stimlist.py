# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from collections import Counter

"""
This module contains the `StimList` class, which is a subclass of the built-in `list` class. The `StimList` class provides methods for generating a pseudo-randomized sequence of stimuli based on an input sequence, experimental condition, and other parameters.

The module also contains a `counter_seq` function that counts the occurrences of each experimental condition in a sequence of pairs.

Example usage:
    input_seq = [[1, 'A'], [2, 'B'], [3, 'A'], [4, 'B']]
    exp_cond = 1
    trial_id = 0
    k = 1
    stim_list = StimList(input_seq, exp_cond, trial_id, k)
    prand_seq = stim_list.prand_seq()
"""

__author__ = "Daniel Diaz"
__copyright__ = "Daniel Diaz 2019"
__license__ = "GPL 3.0"
__version__ = "1.1.0"
__maintainer__ = "Daniel Diaz"
__email__ = "daniel.diaz@ucl.ac.uk"
__status__ = "Production"


def counter_seq(seq_pairs):
    """
    Counts the occurrences of each experimental condition in a sequence of pairs.

    :param seq_pairs: A list of pairs, where each pair contains a trial ID and an experimental condition.
    :return: A list of lists, where each inner list contains an experimental condition and its count.
    """
    seq_cond_count = Counter([pair_id_cond[1] for pair_id_cond in seq_pairs]).items()

    return [list(pair_cond_count) for pair_cond_count in seq_cond_count]


class StimList(list):
    """
    A class for generating pseudo-random sequences from an input list.

    This class extends the built-in `list` class and provides methods for generating pseudo-random sequences based on an input list of data. The input list is expected to be in CSV format, with columns for trial IDs and experimental conditions.

    The class uses a custom algorithm to generate the pseudo-random sequences, which takes into account the specified parameters such as the number of consecutive stimuli with the same condition (`k`) and the column indices for the trial IDs and experimental conditions.

    Parameters
    ----------
        input_seq : list[list]
            Input List
        exp_cond : int
            Index of Experimental condition column
        trial_id=0 : int
            Index of Trial-ID/Number column
        k=1 : int
            Number of consecutive repetitions of exp_cond
    """

    def __init__(self, input_seq, exp_cond, trial_id=0, k=1):
        """
        Initializes a new `StimList` object with the given input sequence and parameters.

        :param input_seq: The input sequence of data in CSV format.
        :param exp_cond: The index of the column containing the experimental condition.
        :param trial_id: The index of the column containing the trial ID. Default is 0.
        :param k: The number of consecutive stimuli with the same condition. Default is 1.
        """
        super(StimList, self).__init__()
        # Instance variables
        self.input_seq = input_seq
        self.exp_cond = exp_cond
        self.trial_id = trial_id
        self.k = k

        # Check correct input values.
        if not input_seq:
            raise ValueError('input list is empty')

        if k < 1:
            raise ValueError('k value should be 1 or more')

        if exp_cond == trial_id:
            raise ValueError('trial_id column and exp_cond column should be different')

        if exp_cond < 0 or trial_id < 0:
            raise ValueError('Python indexes start from 0')

        if exp_cond >= len(input_seq[0]) or trial_id >= len(input_seq[0]):
            raise ValueError('trial_id column or exp_cond column index are out of range')

        if (len(list(zip(*input_seq))[trial_id]) !=
                len(set(list(zip(*input_seq))[trial_id]))):
            raise ValueError('trial_id column contains duplicates')

        # Output sequence
        self.out_seq = []

        # Merged output sequence
        self.sorted_seq = []

    def prand_seq(self):
        """
        Generates a pseudo-random sequence from the input list.

        This method uses a custom algorithm to generate a pseudo-random sequence based on the input list and the specified parameters. The generated sequence is returned as a list.

        :return: A pseudo-random sequence generated from the input list.
        """
        # First step is to create a sequence with pairs: trial_id, exp_cond
        simple_seq = self.__redux_seq()

        # Check feasibility of the task with the input list and actual parameters
        init_cond_count = counter_seq(simple_seq)
        init_check = self.__feasibility_test(init_cond_count)
        if not init_check:
            raise ValueError('input list CAN NOT be pseudo randomized with actual parameters')

        print('INFO: Input list can be pseudo randomized with current parameters')

        for _ in self.input_seq:

            if len(simple_seq) == self.k:
                random.shuffle(simple_seq)
                self.out_seq.extend(simple_seq)
                break

            self.out_seq.append(self.__random_jump(simple_seq))

        self.__merge_seq()

        return self.sorted_seq

    def __feasibility_test(self, seq_cond_count):
        """
        Checks whether it is feasible to generate a pseudo-random sequence from the input list.

        This method uses a custom algorithm to determine whether it is possible to generate a pseudo-random sequence from the input list based on the specified parameters. It returns `True` if it is feasible to generate a pseudo-random sequence, and `False` otherwise.

        :param seq_cond_count: A list of lists containing experimental conditions and their counts.
        :return: `True` if it is feasible to generate a pseudo-random sequence, `False` otherwise.
        """
        counters = [list(cond_count) for cond_count in zip(*seq_cond_count)][1]
        counters.sort(reverse=True)

        return self.k * sum(counters[1:]) >= (counters[0] - self.k)

    def __merge_seq(self):
        """
        Merges the generated pseudo-random sequence with the input list.

        This method merges the generated pseudo-random sequence with the input list to produce the final output sequence. The merged sequence is stored in the `sorted_seq` instance variable.
        """
        for i in self.out_seq:
            for j in self.input_seq:
                if i[self.trial_id] == j[self.trial_id]:
                    self.sorted_seq.append(j)

    def __redux_seq(self):
        """
        Reduces the input list to a sequence of pairs containing trial IDs and experimental conditions.

        This method reduces the input list to a sequence of pairs, where each pair contains a trial ID and an experimental condition. The reduced sequence is returned as a list of lists.

        :return: A list of lists containing pairs of trial IDs and experimental conditions.
        """
        seq_pairs = list(zip(list(zip(*self.input_seq))[self.trial_id],
                             list(zip(*self.input_seq))[self.exp_cond]))

        return [list(pair_id_cond) for pair_id_cond in seq_pairs]

    def __random_jump(self, simple_seq):
        """
        Selects a random element from the given sequence and checks its feasibility.

        This method selects a random element from the given sequence and checks whether it is feasible to include it in the generated pseudo-random sequence based on the specified parameters. If the selected element is feasible, it is returned. Otherwise, another element is selected and the process is repeated until a feasible element is found.

        :param simple_seq: The input sequence of pairs containing trial IDs and experimental conditions.
        :return: A feasible element selected from the input sequence.
        """
        out_seq_count = dict(counter_seq(self.out_seq[-self.k:]))

        while simple_seq:
            candidate = random.choice(simple_seq)
            simple_seq.remove(candidate)
            seq_cond_count = counter_seq(simple_seq)

            if (not self.out_seq or
                    not candidate[1] in out_seq_count or
                    out_seq_count[candidate[1]] + 1 <= self.k):

                if self.__feasibility_test(seq_cond_count):
                    return candidate

            simple_seq.append(candidate)
