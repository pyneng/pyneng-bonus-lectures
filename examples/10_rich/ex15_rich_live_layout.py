import re
from pprint import pprint
import time
import random

import yaml
from rich import print
from rich.tree import Tree
from rich.live import Live
from rich.padding import Padding
from rich.table import Table
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.pretty import pretty_repr
from rich import box

from topology_explorer import parse_cdp, connect_ssh


def generate_tree_from_schema(schema):
    tree = Tree("Topology")
    for s_dev, d_dev_params in schema.items():
        s_dev_tree = tree.add(s_dev)
        for d_dev, params in d_dev_params.items():
            s_dev_tree.add(d_dev)
    return Panel(Padding(tree, 4), title="Current topology")


def generate_log_table(data):
    new_data = "\n".join(data)
    data = new_data.split("\n")
    c = Console()
    last_n = c.size.height - 10
    log_table = Table(expand=True, show_header=False, show_footer=False, box=box.SIMPLE)
    log_table.add_column("Script execution log")
    for row in data[-last_n:]:
        log_table.add_row(row)
    return Panel(log_table, title="Execution log")


def make_layout():
    log_table = Table()
    log_table.add_column("")
    layout = Layout(name="root")

    layout.split_row(
        Layout(name="log", ratio=2),
        Layout(name="tree"),
    )
    layout["tree"].update(generate_tree_from_schema({}))
    layout["log"].update(generate_log_table([]))
    return layout


def explore_topology(start_device_ip, params, layout=None):
    log_table = []  # Rich
    if layout:
        print = log_table.append

    visited_hostnames = set()
    visited_ipadresses = set()
    topology = {}
    todo = []
    todo.append(start_device_ip)

    while len(todo) > 0:
        # live.update(generate_tree_from_schema(topology)) # Rich
        layout["tree"].update(generate_tree_from_schema(topology))
        layout["log"].update(generate_log_table(log_table))
        current_ip = todo.pop(0)
        params["host"] = current_ip

        result = connect_ssh(params, "sh cdp neig det", log=log_table)
        if not result:
            continue
        current_host, sh_cdp_neighbors_output = result
        neighbors = parse_cdp(sh_cdp_neighbors_output)
        print("\nFound neighbors")
        print(pretty_repr(neighbors))

        topology[current_host] = neighbors
        visited_ipadresses.add(current_ip)
        visited_hostnames.add(current_host)

        for neighbor, n_data in neighbors.items():
            neighbor_ip = n_data["ip"]
            if (
                neighbor not in visited_hostnames
                and neighbor_ip not in visited_ipadresses
                and neighbor_ip not in todo
            ):
                print(f"New neighbor {neighbor_ip}")
                todo.append(neighbor_ip)
    return topology


def make_pretty(start, common_params):
    layout = make_layout()
    with Live(layout, refresh_per_second=10) as live:  # Rich
        topology = explore_topology(start, common_params, layout)


if __name__ == "__main__":
    common_params = {
        "auth_password": "cisco",
        "auth_secondary": "cisco",
        "auth_strict_key": False,
        "auth_username": "cisco",
        "platform": "cisco_iosxe",
        "timeout_socket": 5,
        "timeout_transport": 10,
    }
    start = "192.168.100.1"
    make_pretty(start, common_params)
