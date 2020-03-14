from typing import Literal


def get_data_by_key_value(
    db_name: str, key: Literal["mac", "ip", "vlan", "interface"], value: str
) -> str:
    return "line"


print(get_data_by_key_value("database.db", "ip", "8.8.8.8"))
