from promqlpy import split_binary_op


def test_simple_slit():
    assert split_binary_op('sum(rate(foo{bar="baz"}[5m])) by (job) > 0') == {
        "code": 'sum(rate(foo{bar="baz"}[5m])) by (job) > 0',
        "is_binary_op": True,
        "left": {
            "code": 'sum(rate(foo{bar="baz"}[5m])) by (job)',
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_bool():
    assert split_binary_op(
        'sum(rate(foo{bar="baz"}[5m])) by (job) >bool 0'
    ) == {
        "code": 'sum(rate(foo{bar="baz"}[5m])) by (job) > bool 0',
        "is_binary_op": True,
        "left": {
            "code": 'sum(rate(foo{bar="baz"}[5m])) by (job)',
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_on():
    assert split_binary_op(
        'sum(rate(foo{bar="baz"}[5m])) by (job) >on(job) 0'
    ) == {
        "code": 'sum(rate(foo{bar="baz"}[5m])) by (job) > on (job) 0',
        "is_binary_op": True,
        "left": {
            "code": 'sum(rate(foo{bar="baz"}[5m])) by (job)',
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_multi_logic():
    assert split_binary_op("a and b and c or d or f and e") == {}
