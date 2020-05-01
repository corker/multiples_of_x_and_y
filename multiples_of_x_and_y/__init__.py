import sys
from .calculator import calculate
from .file_reader import read_file
from .file_writer import write_file

def run(input_file_path, output_file_path):
    inputs = read_file(input_file_path)
    outputs = (calculate(input[0], input[1], input[2]) for input in inputs)
    write_file(output_file_path, outputs)
