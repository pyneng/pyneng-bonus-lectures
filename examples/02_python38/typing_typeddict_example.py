from typing import TypedDict, NamedTuple


class IPAddress(NamedTuple):
    ip: str
    mask: int = 24


ip1 = IPAddress("10.1.1.1", 28)

# IPAddress(ip='10.1.1.1', mask=28)


class IPAddress(TypedDict):
    ipaddress: str
    mask: int


ip1 = IPAddress(ipaddress="8.8.8.8", mask=26)
