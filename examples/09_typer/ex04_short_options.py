from typing import List
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
    ip_list: List[str],
    username: str = typer.Option(...),
    password: str = typer.Option(..., "--password", "-p"),
    secret: str = typer.Option(..., "-s", help="Enable password"),
):
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }

    device_list = [{**device_params, "host": ip} for ip in ip_list]

    result_dict = send_command_to_cisco_devices(device_list, command)
    for ip, output in result_dict.items():
        print(ip.center(30, "="))
        print(output)


if __name__ == "__main__":
    typer.run(main)
