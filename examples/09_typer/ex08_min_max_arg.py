from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from typing import Optional

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
    params_file: typer.FileText,
    output_file: typer.FileTextWrite,
    max_threads: int = typer.Argument(..., min=1, max=50, clamp=True),
):
    print(f"{command=} {params_file=} {output_file=} {max_threads=}")
    devices = yaml.safe_load(params_file)
    results = send_command_to_devices(devices, command, max_threads)
    if output_file:
        for line in results:
            output_file.write(line + "\n")
    else:
        pprint(results)


if __name__ == "__main__":
    typer.run(cli)
