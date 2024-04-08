import click
from tools.uwp import UWP
from tools.subsector import Subsector
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def main():
    pass

@main.command()
def uwp():
    uwp = UWP()
    console.print(uwp)

@main.command()
def subsector():
    subsector = Subsector()
    table = Table()

    table.add_column("Position", justify="right")
    table.add_column("UWP", justify="right")

    for (pos, uwp) in subsector.worlds:
        table.add_row(pos, str(uwp))

    console.print(table)

main()
