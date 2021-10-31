Pseudo Random List Generator (PRLGEN)
====================================

This is a **Python 3.6+** compatible *package* that can be used to create offline
pseudo randomised stimuli lists for Psycholinguistics experiments.

It is a command line tool that expects as arguments:

- An input **CSV** file.
- The column index that stores the unique **trial ID** (an integer).
- The column index that stores the **experimental condition** (an integer).
- How many *consecutive stimulus of the same experimental condition* you want to allow (minimum is one).
- How many *output files* you want to generate (minimum is one).

It will create the output files in the same folder as the input file.

It is possible to use this package inside your own **python compatible stimuli presentation software**.
Examples are: **PsychoPy**
(`https://www.psychopy.org/ <https://www.psychopy.org/>`__) and others like:
`Presentations <https://www.neurobs.com/>`__,
`EyeLink <https://www.sr-research.com/experiment-builder/>`__ or
`PyGaze <http://www.pygaze.org/>`__.

**PsychoPy** is a free cross-platform package allowing you to run a wide
range of experiments in the behavioral sciences (neuroscience,
psychology, psychophysics, linguistics...).

This is a critical feature in **psycholinguistics** experiments and it is now available:
sorting on the fly the stimuli from the input list before any of them is
presented whilst avoiding repetitions. The researcher usually needs to show the stimuli in a
randomised order but must not allow **consecutive trials of the same
experimental condition**.

**Example code is available** in the examples folder to show how to add it to your PsychoPy
project. The output list is ready to be used in your main presentation
loop. It won't change the column order or touch any row content. It will
shuffle the order of the items in the list to match the pseudo random
criteria.

The **module interface** (check the example and comments in the example code) allows the user
to set the parameters:

- The input list, as a *list of list* in Python ``[[list], [list], ...]``. Usually it is parsed from an input *CSV* file.
- The column index of the list with unique **trial id**, or *trial number*. By *default*, the value is the first column or column **zero**.
- The column index that stores the **experimental condition** code. It has to be different than the *trial id* index.
- The number of consecutive stimuli of the same condition that can appear in the output list. By *default*, the value is **one**.

This last parameter can be set above one. It may be desirable when the input list is
populated with different *fillers* as experimental conditions and they
don't match the same number of items as the other conditions.

The module assumes **by default** that **the trial number column** is
the **first column** of the list and the desired **repetition is 1**
(one), that is, you don't want more than 1 trial of the same condition
being presented consecutively.

**The module** will *check* if the number of items in each experimental
condition are **enough** to build a pseudo random list with the desired
*repetition parameter*. It will trigger an error and **stop your script if
the list is impossible to build** and it will inform you about the
problem. Furthermore, an incorrect trial number column, i.e., not unique
values in each row, an incorrect experimental condition column, or zero or negative
values for the repetition, will trigger an error and stop the script.

The code is released as GPL v3.0 to allow it to be integrated with
PsychoPy.

A **proof of correctness** of the algorithm is available as a Latex document
in the proof folder. Thus, it is possible to implement the algorithm in any other
programing language with enough expression power. The tests code implements the function
described in the proof document under the correctness paragraph for *k consecutive elements*.
Any new implementation should also validate the correctness using the same function
in the target language.
