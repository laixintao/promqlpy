"""
usage:
Change the ./dist to https://github.com/samber/awesome-prometheus-alerts location
"""
import os
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load():
    exprs = []
    for root, _, files in os.walk("./dist", topdown=False):
        for file in files:
            path = os.path.join(root, file)
            if not path.endswith(".yaml") and not path.endswith(".yml"):
                continue
            if file == "template.yml":
                continue
            print(f"parse {path}...")
            with open(path) as yamlf:
                data = yaml.load(yamlf, Loader=Loader)
                groups = data.get("groups", [])
                for group in groups:
                    rules = group.get("rules", [])
                    if not rules:
                        continue
                    for rule in rules:
                        exprs.append(rule["expr"])

    return exprs


def save(exprs):
    with open("rules.txt", "w+") as target:
        target.write("\n".join(exprs))


a = load()
save(a)
