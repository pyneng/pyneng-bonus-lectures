from platform import system as system_name
from pprint import pprint
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException
from rich.progress import Progress
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "success" : "bold blue",
    "fail" : "bold red",
    "error": "bold yellow",
    "repr.str": "bold white",
    #"repr.number": "bold green", # defaults: python -m rich.theme
})
console = Console(theme=custom_theme)
total_dev = 4
progress = Progress(console=console)
t1 = progress.add_task("Пингую...", total=total_dev)
t2 = progress.add_task("Успешное подключение...", total=total_dev)
t3 = progress.add_task("Ошибка при подключении...", total=total_dev)


def ping_ip(ip):
    param = "-n" if system_name().lower() == "windows" else "-c"
    command = ["ping", param, "3", ip]
    reply = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    progress.update(t1, advance=1)
    ip_is_reachable = reply.returncode == 0
    return ip, ip_is_reachable


def send_show(device, command):
    ip = device["host"]
    console.log(f"Подключаюсь к {ip}")
    try:
        with Scrapli(**device) as ssh:
            progress.update(t2, advance=1)
            console.log(f"Подключение успешно {ip}", style="success")
            reply = ssh.send_command(command)
            output = reply.result
            return output
    except ScrapliException as error:
        console.log(error, ip, style="fail")
        progress.update(t3, advance=1)


def ping_and_send_show_to_devices(devices, command, limit=10):
    results = []
    ip_dict = {dev["host"]: dev for dev in devices}
    unreachable_ip = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_list_show = [executor.submit(send_show, dev, command) for dev in devices]
        future_list_ping = [executor.submit(ping_ip, ip) for ip in ip_dict]
        for f in as_completed(future_list_ping + future_list_show):
            status = f.result()
    return results


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    with progress:
        output = ping_and_send_show_to_devices(devices, "sh clock")
    console.log(output)

