import sqlite3
from typing import Final

DATABASE: Final[str] = "dhcp_snooping.db"


def create_db(db_name: str, schema: str) -> None:
    with open(schema) as f:
        schema_f = f.read()
        connection = sqlite3.connect(db_name)
        connection.executescript(schema_f)
        connection.close()


if __name__ == "__main__":
    DATABASE = "mydb.db"
    schema_filename = "dhcp_snooping_schema.sql"
    create_db(DATABASE, schema_filename)
