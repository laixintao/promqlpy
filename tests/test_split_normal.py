from promqlpy import split_binary_op


def test_simple_slit():
    assert split_binary_op('sum(rate(foo{bar="baz"}[5m])) by (job) > 0') == {
        "is_binary_op": True,
        "left": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": 'sum(rate(foo{bar="baz"}[5m])) by (job)',
        },
        "right": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "0",
        },
        "op": ">",
        "group_modifier": {"op": "", "args": None},
        "join_modifier": {"op": "", "args": None},
        "code": 'sum(rate(foo{bar="baz"}[5m])) by (job) > 0',
    }


def test_bool():
    assert (
        split_binary_op('sum(rate(foo{bar="baz"}[5m])) by (job) >bool 0')
    ) == {
        "is_binary_op": True,
        "left": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": 'sum(rate(foo{bar="baz"}[5m])) by (job)',
        },
        "right": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "0",
        },
        "op": ">",
        "group_modifier": {"op": "", "args": None},
        "join_modifier": {"op": "", "args": None},
        "code": 'sum(rate(foo{bar="baz"}[5m])) by (job) > bool 0',
    }


def test_on():
    result = split_binary_op(
        'sum(rate(foo{bar="baz"}[5m])) by (job) >on(job) 0'
    )
    assert result == {
        "is_binary_op": True,
        "left": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": 'sum(rate(foo{bar="baz"}[5m])) by (job)',
        },
        "right": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "0",
        },
        "op": ">",
        "group_modifier": {"op": "on", "args": ["job"]},
        "join_modifier": {"op": "", "args": None},
        "code": 'sum(rate(foo{bar="baz"}[5m])) by (job) > on (job) 0',
    }


def test_logic_priority():
    assert split_binary_op("a and b or c") == {
        "is_binary_op": True,
        "left": {
            "is_binary_op": True,
            "left": {
                "is_binary_op": False,
                "left": None,
                "right": None,
                "op": "",
                "group_modifier": {"op": "", "args": None},
                "join_modifier": {"op": "", "args": None},
                "code": "a",
            },
            "right": {
                "is_binary_op": False,
                "left": None,
                "right": None,
                "op": "",
                "group_modifier": {"op": "", "args": None},
                "join_modifier": {"op": "", "args": None},
                "code": "b",
            },
            "op": "and",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "a and b",
        },
        "right": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "c",
        },
        "op": "or",
        "group_modifier": {"op": "", "args": None},
        "join_modifier": {"op": "", "args": None},
        "code": "(a and b) or c",
    }


def test_multi_comapre_op():
    code = "a > 10 < b"
    result = split_binary_op(code)
    assert result == {
        "is_binary_op": True,
        "left": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "a > 10",
        },
        "right": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "b",
        },
        "op": "<",
        "group_modifier": {"op": "", "args": None},
        "join_modifier": {"op": "", "args": None},
        "code": "(a > 10) < b",
    }
