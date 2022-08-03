# promqlpy

Promqlpy is a python library for parsing PromQL/MetricsQL.

## Install

Requirements: golang

This project is based on [metricsql](github.com/VictoriaMetrics/metricsql),
works by calling golang function via `cffi` and CGO from Python.

install via pip:

```bash
$ pip install promqlpy
```

Current features:

### Split Alert Rules

Using `split_binary_op` function, we can split an
[Alert Rule](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
into multiple expression.

```python
>>> from promqlpy import split_binary_op
>>> split_binary_op('sum(rate(foo{bar="baz"}[5m])) by (job) > 0')
{'left': {'left': None, 'right': None, 'op': '', 'code': 'sum(rate(foo{bar="baz"}[5m])) by (job)', 'is_binary_op': False}, 'right': {'left': None, 'right': None, 'op': '', 'code': '0', 'is_binary_op': False}, 'op': '>', 'code': 'sum(rate(foo{bar="baz"}[5m])) by (job) > 0', 'is_binary_op': True}
```

Use Cases:

Alert rules work like this: if the result is no value, then it's good. (e.g.
`up < 1` returns no data when normal, but return value if match the condition).
This makes sense for alerting, but when you want to render an diagram for the
alert rules, it will be helpless, because all you see is blank charts with
occasionally some lines (when alerts happened).

The return value of `split_binary_op()`:

This function will take a PromQL/MetricsQL code, then return an `<expression>`,
in Json format, with those values:

- "code": Original code of PromQL/MetricsQL for this <expression>
- "is_binary_op": If it is True, then meaning that it is a binary expression,
  then the `op` field is also set. If it is False, then only the `code` is set,
  meaning that the `<expression>` at this node is just an normal `<expression>`,
  you can render to a chart for that, and `left` `right` is set to None, `op`
  set to empty string `""`.
- "op": Only be set when the current `<expression>` at this node is Binary Op
  Expression. Possible values are:
  - Compare(When `op` is one of Compare, then `left` and `right` can only a
    regular expression, not possible to be another Binary Op Expression):
    - == (equal)
    - != (not-equal)
    - `>` (greater-than)
    - < (less-than)
    - `>=` (greater-or-equal)
    - <= (less-or-equal)
  - Logic(When `op` is one of Logic, `left` and `right` cloud be Binary Op
    Expression or Regular Expression, the Json is nested):
    - and
    - or
    - unless
- "left": also a `<expression>`, same structure as the current one
- "right": also a `<expression>`, same structure as the current one

Also please be noted that the `code` will be formatted, but it's semantic level
identical.
