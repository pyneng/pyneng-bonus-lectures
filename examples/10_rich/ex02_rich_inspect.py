import re
from rich import inspect
from data_dicts import hsrp


with open("data_dicts.py") as f:
    inspect(f)
    inspect(f, methods=True)


m = re.search(r"\d+", "vlan 10,20")
inspect(m)
inspect(m, methods=True)

inspect(inspect)
