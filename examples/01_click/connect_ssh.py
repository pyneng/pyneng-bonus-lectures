import click
from netmiko import ConnectHandler
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


@click.command()
@click.argument("command")
@click.argument("ip-list", nargs=-1)
@click.option("--username", "-u", envvar="NETMIKO_USER")
@click.option("--password", "-p", envvar="NETMIKO_PASSWORD")
@click.option("--secret", "-s", envvar="NETMIKO_SECRET")
def main(command, ip_list, username, password, secret):
    device_params = {"device_type": "cisco_ios"}
    local_vars = locals()

    for param in ("username", "password", "secret"):
        if not local_vars[param]:
            value = click.prompt(f"Введите {param}")
            device_params[param] = value
        else:
            device_params[param] = local_vars[param]

    for ip in ip_list:
        device_params["host"] = ip
        print(send_show_command(device_params, command))


if __name__ == "__main__":
    main()
