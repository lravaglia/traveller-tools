import click
from tools.uwp import UWP
from tools.subsector import Subsector
from rich import print


@click.group()
def main():
    pass

@main.command()
def uwp():
    print(UWP())

@main.command()
def subsector():
    print(Subsector())

main()
