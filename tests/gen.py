import sys
from promqlpy import split_binary_op

file_path = sys.argv[1]
with open(file_path) as rules_txt:
    for line in rules_txt:
        result = split_binary_op(line)
