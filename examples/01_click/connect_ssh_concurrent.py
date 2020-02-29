import click
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint

from netmiko import ConnectHandler
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_devices(devices, command, limit):
    results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [
            executor.submit(send_show_command, device, command)
            for device in devices
        ]
        with click.progressbar(length=len(futures), label="Connecting to devices") as bar:
            for future in as_completed(futures):
                results.append(future.result())
                bar.update(1)
    return results


@click.command()
@click.argument("command")
@click.option("--yaml-params", "-y", "yaml_file", type=click.File('r'), required=True)
@click.option("--threads", "-t", type=click.IntRange(1, 10), required=True)
def main(command, yaml_file, threads):
    devices = yaml.safe_load(yaml_file)
    pprint(send_command_to_devices(devices, command, limit=threads))


if __name__ == "__main__":
    main()
