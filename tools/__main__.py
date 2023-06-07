import click
from uwp import Uwp
from subsector import Subsector


@click.group()
def main():
    pass

@click.command()
def uwp():
    print(Uwp())

@click.command()
def subsector():
    print(Subsector())

main.add_command(uwp)
main.add_command(subsector)

main()