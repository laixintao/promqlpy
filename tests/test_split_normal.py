from promqlpy import split


def test_simple_slit():
    assert split('sum(rate(foo{bar="baz"}[5m])) by (job) > 0') == {
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
