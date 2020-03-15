import re

regex = "vlan (\d+) is flapping between port (\S+) and port (\S+)"

ports = set()

with open("log.txt") as f:
    for line in f:
        if (match := re.search(regex, line)) :
            vlan, port1, port2 = match.groups()
            ports.update({port1, port2})

print(f"Петля между портами {', '.join(ports)}")
