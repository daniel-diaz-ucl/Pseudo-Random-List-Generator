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


def test_output():
    test_list = create_list()
    assert test_list == [['2', 'car', 'Blue'], ['19', 'car', 'Blue'], ['6', 'car', 'Blue'], ['8', 'car', 'Red'], ['23', 'car', 'Blue'], ['16', 'car', 'Blue'], ['17', 'car', 'Blue'], ['10', 'car', 'Red'], ['1', 'car', 'Blue'], ['15', 'car', 'Blue'], ['3', 'car', 'Blue'], ['9', 'car', 'Red'], ['4', 'car', 'Blue'], ['21', 'car', 'Blue'], ['20', 'car', 'Blue'], ['11', 'car', 'Red'], ['22', 'car', 'Blue'], ['14', 'car', 'Blue'], ['18', 'car', 'Blue'], ['7', 'car', 'Red'], ['12', 'car', 'Blue'], ['13', 'car', 'Blue'], ['5', 'car', 'Blue']]
