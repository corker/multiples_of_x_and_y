

def read_file(path):
    lines = (line for line in open(path))
    parsed_lines = (parse_line(line) for line in lines)
    return filter_lines(parsed_lines)

def parse_line(line):
    values = (value for value in line.split(' '))
    filtered_values = filter_values(values)
    parsed_values = (int(value) for value in filtered_values)
    return tuple(parsed_values)

def filter_values(values):
    for value in values:
        if value.strip():
            yield value

def filter_lines(lines):
    for line in lines:
        if line:
            yield line
