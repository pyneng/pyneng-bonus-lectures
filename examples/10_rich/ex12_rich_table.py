from rich.console import Console
from rich.table import Table

from data_dicts import vrf

table = Table()
for name in "vrf param details".split():
    table.add_column(name, justify="left")

for vrf_name, params in vrf.items():
    for index, (param, details) in enumerate(params.items()):
        if type(details) == str:
            details = [details]
        if index == 0:
            table.add_row(vrf_name, param, "\n".join(details))
        else:
            table.add_row("", param, "\n".join(details))

console = Console()
console.print(table)
# console = Console()
# with console.capture() as capture:
#     console.print(table)
# str_output = capture.get()
# print(str_output)
#
# with open("table_output.txt", "w") as f:
#     f.write(str_output)



