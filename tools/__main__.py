import click
from uwp import Uwp
from subsector import Subsector
from rich import print


@click.group()
def main():
    pass

@main.command()
def uwp():
    print(Uwp())

@main.command()
def subsector():
    print(Subsector())

main()
