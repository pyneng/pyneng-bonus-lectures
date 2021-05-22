from enum import Enum
import click
import typer
from typing import List


# Default values:
DFLT_DB_NAME = "dhcp_snooping.db"
DFLT_DB_SCHEMA = "dhcp_snooping_schema.sql"


class DatabaseKeys(str, Enum):
    mac = "mac"
    ip = "ip"
    vlan = "vlan"
    intf = "interface"
    switch = "switch"

app = typer.Typer()

@app.command()
def create(
    db_filename: str = typer.Option(DFLT_DB_NAME, "--db", help="DB filename"),
    db_schema: str = typer.Option(DFLT_DB_SCHEMA, help="DB schema filename"),
):
    """
    create DB
    """
    print("Creating DB {} with DB schema {}".format(db_filename, db_schema))


@app.command()
def add(
    filename: List[str],
    db_filename: str = typer.Option(DFLT_DB_NAME, "--db", help="DB filename"),
    switch_data: bool = False,
):
    """
    add data to db from FILENAME
    """
    print(filename, db_filename, switch_data)
    if switch_data:
        print("Adding switch data to database")
    else:
        print("Reading info from file(s) {}".format(", ".join(filename)))
        print("Adding data to db {}".format(db_filename))


@app.command()
def get(
    key: DatabaseKeys = typer.Option(DatabaseKeys.intf),
    value: str = "",
    show_all: bool = True,
):
    """
    get data from db
    """
    if key and value:
        print("Geting data from DB: {}".format(db_filename))
        print("Request data for host(s) with {} {}".format(key, value))
    elif show_all:
        print("Showing {} content...".format(db_filename))


if __name__ == "__main__":
    app()
