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
@click.option("--yaml-params", "-y", type=click.File('r'))
@click.option("--write-output-to-file", "-o", type=click.File('w'))
def main(command, yaml_params, write_output_to_file):
    if yaml_params:
        devices = yaml.safe_load(yaml_params)

    for dev in devices:
        if write_output_to_file:
            write_output_to_file.write(send_show_command(dev, command))
        else:
            print(send_show_command(dev, command))


if __name__ == "__main__":
    main()
