"""
usage:
python tests/gen.py tests/data/awesome_prometheus_alerts.txt tests/test_awesome_rules.py
args: source rule file (one at a line) generate_target.py
"""
import sys
import pprint
from promqlpy import split_binary_op


file_path = sys.argv[1]
generate_test = sys.argv[2]

with open(generate_test, "r") as f:
    exist = f.read()

testfile = open(generate_test, "a+")

TEMPLATE = """
def test_case_{index}():
    assert split_binary_op('{code}') == {expected}

"""

with open(file_path) as rules_txt:
    lines = rules_txt.readlines()


def generate(line, count):
    if f"test_case_{count}" in exist:
        return

    print("=" * 20 + f"test_{count}")
    actual = split_binary_op(line)
    print(line)
    pprint.pprint(actual)
    confirm = input("expected? y/n: ")
    if "y" == confirm:
        testfile.write(
            TEMPLATE.format(
                index=count,
                code=line.strip(),
                expected=pprint.pformat(actual, indent=4),
            )
        )


count = 0
for line in lines:
    generate(line, count)
    count += 1
