from promqlpy import split

a = split('sum(rate(foo{bar="baz"}[5m])) by (job) > 0')
print(a)

count = 0
while 1:
    with open("tests/data/awesome_prometheus_alerts.txt", "r") as rulesfile:
        for line in rulesfile:
            count += 1
            split(line)
            print(count)
