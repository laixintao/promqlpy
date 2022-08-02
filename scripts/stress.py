from promqlpy import split_binary_op

a = split_binary_op('sum(rate(foo{bar="baz"}[5m])) by (job) > 0')
print(a)

count = 0
while 1:
    with open("tests/data/awesome_prometheus_alerts.txt", "r") as rulesfile:
        for line in rulesfile:
            count += 1
            split_binary_op(line)
            print(count)
