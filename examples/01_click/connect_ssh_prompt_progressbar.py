import click
from netmiko import ConnectHandler
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_cisco_devices(device_list, command):
    result = {}
    with click.progressbar(device_list, label="Connecting to devices") as bar:
        for device in bar:
            ip = device["host"]
            result[ip] = send_show_command(device, command)
    return result


@click.command()
@click.argument("command")
@click.argument("ip-list", nargs=-1)
@click.option("--username", "-u", prompt=True)
@click.option("--password", "-p", prompt=True, hide_input=True)
@click.option("--secret", "-s", prompt=True, hide_input=True)
def main(command, ip_list, username, password, secret):
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }
    device_list = [{**device_params, "host": ip} for ip in ip_list]

    result_dict = send_command_to_cisco_devices(device_list, command)
    for ip, output in result_dict.items():
        print("="*30, ip)
        print(output)


if __name__ == "__main__":
    main()

# python connect_ssh_prompt.py "sh ip int br" 192.168.100.1 192.168.100.2 192.168.100.3 192.168.100.1 192.168.100.2 192.168.100.3 -u cisco -p cisco -s cisco
