from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint

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


def main(
    command: str,
    yaml_file: typer.FileText = "devices.yaml",
    threads: int = typer.Option(10, max=50, clamp=True),
):
    devices = yaml.safe_load(yaml_file)
    pprint(send_command_to_devices(devices, command, limit=threads))


if __name__ == "__main__":
    typer.run(main)
