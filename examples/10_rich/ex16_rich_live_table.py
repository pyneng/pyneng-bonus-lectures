import re
from pprint import pprint

import yaml
from scrapli import Scrapli
from scrapli.exceptions import (
    ScrapliException,
    ScrapliAuthenticationFailed,
    ScrapliConnectionError,
)
from rich import print
from rich.live import Live
from rich.padding import Padding
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich import box


def generate_stats_table(stats_data):
    table = Table(show_header=False, show_footer=False, box=box.SIMPLE)
    for name, count in stats_data.items():
        table.add_row(name, str(count))
    return Panel(table)


custom_theme = Theme(
    {
        "success": "bold blue",
        "fail": "bold red",
        "error": "bold yellow",
    }
)
console = Console(theme=custom_theme)
stats_data = {"success": 0, "failed to connect": 0, "auth error": 0}
live = Live(
    generate_stats_table(stats_data), refresh_per_second=4, console=console
)


def send_show(device, command):
    ip = device["host"]
    console.log(f"Подключаюсь к {ip}")
    live.update(generate_stats_table(stats_data))  # Rich
    try:
        with Scrapli(**device) as ssh:
            stats_data["success"] += 1
            console.log(f"Подключение успешно {ip}", style="success")
            reply = ssh.send_command(command)
            output = reply.result
        return output
    except ScrapliAuthenticationFailed as error:
        console.log(error, ip, style="fail")
        if "Timed out connecting to host" in str(error):
            stats_data["failed to connect"] += 1
        else:
            stats_data["auth error"] += 1


def send_show_to_devices(devices, commands):
    results = {}
    for dev in devices:
        output = send_show(dev, commands)
        console.log(output)
        results[dev["host"]] = output
        console.rule(f"Device {dev['host']} DONE")
    return results


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    with live:  # Rich
        output = send_show_to_devices(devices, "sh ip int br")
