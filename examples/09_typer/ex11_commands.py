from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from typing import Optional, List

from netmiko import ConnectHandler
import yaml
import typer

from func02_connect_to_devices import send_show_command, send_command_to_devices


app = typer.Typer()

@app.command("file", help="Read params from file")
def params_from_file(
    command: str,
    ssh_params: typer.FileText,
    max_threads: int = typer.Option(10, min=1, max=50, clamp=True),
):
    devices = yaml.safe_load(ssh_params)
    result_dict = send_command_to_cisco_devices(devices, command)
    pprint(result_dict)


@app.command(help="Enter params as options/input")
def options(
    command: str,
    ip_list: List[str],
    username: str = typer.Option(..., "-u", "--username", prompt=True),
    password: str = typer.Option(
        ..., "-p", "--password", prompt=True, hide_input=True
    ),
    enable_password: str = typer.Option(
        ..., "-e", "--enable", prompt=True, hide_input=True
    ),
    max_threads: int = typer.Option(10, min=1, max=50, clamp=True),
):
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": enable_password,
    }
    device_list = [{**device_params, "host": ip} for ip in ip_list]

    results = send_command_to_devices(device_list, command, max_threads)
    pprint(results)


if __name__ == "__main__":
    app()
