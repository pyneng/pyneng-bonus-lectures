from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from itertools import repeat
import logging

import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

### stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "{asctime} - {name} - {levelname} - {message}", datefmt="%H:%M:%S", style="{"
)
console.setFormatter(formatter)

log.addHandler(console)

### File
logfile = logging.FileHandler("logfile3.log")
logfile.setLevel(logging.WARNING)
formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{")
logfile.setFormatter(formatter)

log.addHandler(logfile)


def send_show(device, show_commands):
    host = device["host"]
    if type(show_commands) == str:
        show_commands = [show_commands]
    cmd_dict = {}
    log.info(f">>> Connecting to {host}")
    try:
        with Scrapli(**device) as ssh:
            for cmd in show_commands:
                reply = ssh.send_command(cmd)
                cmd_dict[cmd] = reply.result
        log.info(f"<<< Received output from {host}")
        return cmd_dict
    except ScrapliException as error:
        #log.exception(error)
        log.critical(f"Error connecting to {host}")


def send_show_to_devices(devices, show, max_threads=10):
    result_dict = {}
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = executor.map(send_show, devices, repeat(show))
        for dev, output in zip(devices, results):
            result_dict[dev["host"]] = output
    return result_dict


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    output = send_show_to_devices(devices, "sh clock")
    pprint(output, width=120)
