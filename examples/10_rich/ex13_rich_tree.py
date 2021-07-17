from rich.tree import Tree
from rich import print

from data_dicts import vrf


tree = Tree("VRF")

for vrf_name, params in vrf.items():
    vrf_tree = tree.add(f"[red]{vrf_name}")
    for param, details in params.items():
        param_tree = vrf_tree.add(f"[green]{param}")
        # param_tree = vrf_tree.add(f"[green]{param}", expanded=False)
        if type(details) == str:
            details = [details]
        for det in details:
            param_tree.add(det)
print(tree)

