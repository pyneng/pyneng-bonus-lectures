from pprint import pprint
import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({
    "success" : "bold blue",
    "fail" : "bold red",
    "error": "bold yellow",
    #"repr.number": "bold green", # defaults: python -m rich.theme
})
console = Console(theme=custom_theme)


def send_show(device, show_commands):
    ip = device["host"]
    console.log(f"Подключаюсь к {ip}")
    if type(show_commands) == str:
        show_commands = [show_commands]
    cmd_dict = {}
    try:
        with Scrapli(**device) as ssh:
            console.log(f"Подключение успешно {ip}", style="success")
            for cmd in show_commands:
                reply = ssh.send_command(cmd)
                cmd_dict[cmd] = reply.result
        return cmd_dict
    except ScrapliException as error:
        console.log(error, ip, style="fail")


def send_show_to_devices(devices, commands):
    results = {}
    with console.status("Working..."):
        for dev in devices:
            output = send_show(dev, commands)
            console.log(output)
            results[dev["host"]] = output
            console.rule(f"Device {dev['host']} DONE")
    return results


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    output = send_show_to_devices(devices, ["sh clock", "sh int desc"])
    console.log(output)


