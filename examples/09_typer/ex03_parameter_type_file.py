from typing import Optional

import typer
from netmiko import ConnectHandler
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_cisco_devices(device_list, command):
    result = {}
    for device in device_list:
        ip = device["host"]
        result[ip] = send_show_command(device, command)
    return result


def main(
    command: str,
    ssh_params: typer.FileText,
    output: Optional[typer.FileTextWrite] = None,
):
    devices = yaml.safe_load(ssh_params)

    result_dict = send_command_to_cisco_devices(devices, command)
    for ip, out in result_dict.items():
        if output:
            output.write(ip.center(30, "=") + "\n")
            output.write(out + "\n")
        else:
            print(ip.center(30, "="))
            print(out)


if __name__ == "__main__":
    typer.run(main)
