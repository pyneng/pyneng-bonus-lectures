from pprint import pprint
import re
import inspect


with open("data_dicts.py") as f:
    pprint(dir(f))
    help(f)


m = re.search(r"\d+", "vlan 10,20")
pprint(dir(m))


def sum(a, b):
    return a + b

print(inspect.getfullargspec(sum))
