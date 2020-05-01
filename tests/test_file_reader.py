import sys
import os
import multiples_of_x_and_y.file_reader as file_reader

def read_file_helper(file_name):
    return file_reader.read_file(os.path.join(os.path.dirname(__file__), file_name))

def test_read_file_example1():
    expected = [
        (1, 2, 3),
        (2, 3, 4)
    ]
    actual = read_file_helper("test_file_reader_example1.txt")
    actual = list(actual)
    assert actual == expected

def test_read_file_example2():
    expected = [
        (1, 2, 3)
    ]
    actual = read_file_helper("test_file_reader_example2.txt")
    assert list(actual) == expected

def test_read_file_example3():
    expected = []
    actual = read_file_helper("test_file_reader_example3.txt")
    assert list(actual) == expected
