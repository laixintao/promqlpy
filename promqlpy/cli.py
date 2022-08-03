"""
testing group:

(kube_pod_container_status_restarts_total - kube_pod_container_status_restarts_total offset 10m >= 1) and ignoring (reason) min_over_time(kube_pod_container_status_last_terminated_reason{reason="OOMKilled"}[10m]) == 1

"""
import sys
from .split import split_binary_op
from rich.tree import Tree
from rich import print
from rich.syntax import Syntax
from rich.panel import Panel


def display(code):
    return Panel(Syntax(code.strip(), "promql", word_wrap=True))


def add_node(tree, expr):
    if expr["is_binary_op"]:
        head = expr["op"]
        gop = expr.get("group_modifier")
        if gop["op"]:
            _op = gop["op"]
            _args = ", ".join(gop["args"])
            head = f"{head} {_op} ({_args})"

        sub_tree = Tree(Panel(head, expand=False))
        add_node(sub_tree, expr["left"])
        add_node(sub_tree, expr["right"])
        tree.add(sub_tree)
    else:
        tree.add(display(expr["code"]))


def main():
    code = sys.stdin.read()
    grammar = split_binary_op(code)
    tree = Tree(display(code))

    add_node(tree, grammar)
    print(tree)


if __name__ == "__main__":
    main()
