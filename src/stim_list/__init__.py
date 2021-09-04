# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to randomly sort a list such as no k consecutive elements share the same exp_cond.
Compatible with PsychoPy and Python 3.6"""


import random
from collections import Counter

__author__ = "Daniel Diaz"
__copyright__ = "Daniel Diaz 2019"
__license__ = "GPL 3.0"
__version__ = "1.0.0"
__maintainer__ = "Daniel Diaz"
__email__ = "daniel.diaz@ucl.ac.uk"
__status__ = "Production"


def counter_seq(seq_pairs):
    """Create a sequence with pairs: exp_cond, count."""
    seq_cond_count = Counter([pair_id_cond[1] for pair_id_cond in seq_pairs]).items()

    return [list(pair_cond_count) for pair_cond_count in seq_cond_count]


class StimList(list):
    """
    Stimulus list to be randomly sorted.

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
        """Constructor with the input parameters"""

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
        Pseudo Random List Sorting Algorithm. To be called after the constructor.
        It returns a sorted list.
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
        """Test to check if the output list can be built."""
        counters = [list(cond_count) for cond_count in zip(*seq_cond_count)][1]
        counters.sort(reverse=True)

        return self.k * sum(counters[1:]) >= (counters[0] - self.k)

    def __merge_seq(self):
        """Merge input_seq and out_seq by common trial_id column and the order of out_seq"""
        for i in self.out_seq:
            for j in self.input_seq:
                if i[self.trial_id] == j[self.trial_id]:
                    self.sorted_seq.append(j)

    def __redux_seq(self):
        """Create a simplified sequence with pairs: trial_id, exp_cond."""
        seq_pairs = list(zip(list(zip(*self.input_seq))[self.trial_id],
                             list(zip(*self.input_seq))[self.exp_cond]))

        return [list(pair_id_cond) for pair_id_cond in seq_pairs]

    def __random_jump(self, simple_seq):
        """Randomised choice selector that checks k cond value and previous attempts."""
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
