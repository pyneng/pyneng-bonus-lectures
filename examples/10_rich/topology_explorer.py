import re
from pprint import pprint

import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException
from rich import print


def parse_cdp(output):
    regex = (
        r"Device ID: (?P<host>\w+)\."
        r".*?"
        r"IP address: (?P<ip>\S+)\n"
        r".*?"
        r"Interface: (?P<local_port>\S+), +"
        r"Port ID \(outgoing port\): (?P<remote_port>\S+)"
    )

    neighbors = {}

    match_iter = re.finditer(regex, output, re.DOTALL)
    for match in match_iter:
        hostname = match.group("host")
        groupdict = match.groupdict()
        del groupdict["host"]
        neighbors[hostname] = groupdict
    return neighbors


def connect_ssh(device, command):
    host = device["host"]
    print(f">>> Connecting to {host}")
    try:
        with Scrapli(**device) as ssh:
            reply = ssh.send_command(command)
            output = reply.result
            prompt = ssh.get_prompt()
            print(f"<<< Received output from {host}")
            hostname = re.search(r"(\S+)[>#]", prompt).group(1)
            return hostname, output
    except ScrapliException as error:
        print(f"Error connecting to {host}")

