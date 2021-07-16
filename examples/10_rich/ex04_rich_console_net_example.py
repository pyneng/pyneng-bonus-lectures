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


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        output = send_show(dev, ["sh clock", "sh int desc"])
        console.log(output)


