from rich.prompt import Prompt, Confirm, IntPrompt


trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]


interface = Prompt.ask("Interface number")
mode = Prompt.ask("Interface mode", choices=["access", "trunk"])
vlan = IntPrompt.ask("VLAN number", default=1)

Confirm.ask("Continue program?")
