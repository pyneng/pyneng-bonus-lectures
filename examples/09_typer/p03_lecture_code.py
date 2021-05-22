from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from typing import Optional, List

from netmiko import ConnectHandler
import yaml
import typer


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_devices(devices, command, limit):
    results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [
            executor.submit(send_show_command, device, command) for device in devices
        ]
        for future in as_completed(futures):
            results.append(future.result())
    return results


def cli(
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
    print(f"{command=} {ip_list=} {username=} {max_threads=}")

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
    typer.run(cli)
