

def write_file(path, outputs):
    with open(path, "w") as fp:
        for output in outputs:
            line = ' '.join([str(value) for value in output]) 
            fp.write(line)
