# Pseudo Random List Sorting Algorithm

This is a **Python 3.6** compatible _module_ for PsychoPy ([https://www.psychopy.org/](https://www.psychopy.org/)) and other **software packages that can interface with Python** (for example: [Presentations](https://www.neurobs.com/), [EyeLink](https://www.sr-research.com/experiment-builder/) or [PyGaze](http://www.pygaze.org/)).

PsychoPy is a free cross-platform package allowing you to run a wide range of experiments in the behavioral sciences (neuroscience, psychology, psychophysics, linguistics...).

The goal is to offer the critical feature in **psycholinguistics** of sorting on the fly the stimuli from the input list before any of them is presented. The researcher usually needs to show the stimuli in a randomised order but not allowing **consecutive trials of the same experimental condition**.

The module interface allows the user to set as parameters the column from the list with unique **trial id**, or trial number, and the column with the **experimental condition** code. Finally, it allows to lessen the restrictions to allow consecutive stimuli of the same condition up to a number. This option may be desirable when the input list is populated with different _fillers_ as experimental conditions and they don't match the same number of items as other experimental conditions.

**Example code is available** to show how to add it to your PsychoPy project. The output list is ready to be used in your main presentation loop. It won't change the column order or touch any row content. It will shuffle the order of the items in the list to match the pseudo random criteria.

**The module** will **check if the number of items in each experimental condition are enough** to build a pseudo random list with the desired repetition parameter. It will trigger an error and **stop your script if the list is impossible to build** and it will inform you what is the problem. Furthermore, an incorrect trial number column, i.e., not unique values in each row, incorrect experimental condition or zero or negative values for the repetition will trigger an error and stop the script.

The module assumes **by default** that **the trial number column** is the **first column** of the list and the desired **repetition is 1** (one), that is, you don't want more than 1 trial of the same condition being presented consecutively. \


The code is released as GPL 3.0 to allow it to be integrated with PsychoPy.

A proof of correctness of the algorithm is available as a Latex document in the proof folder.
