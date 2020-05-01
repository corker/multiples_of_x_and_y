import os
import sys
from multiples_of_x_and_y import run

assert len(sys.argv) == 3, "please provide input_file_path and output_file_path"
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
assert os.path.isfile(input_file_path), "'{}' does not exist".format(input_file_path)
assert not os.path.isfile(output_file_path), "'{}' must not exist".format(output_file_path)
run(input_file_path, output_file_path)