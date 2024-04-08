import rich_click as click
from tools.uwp import UWP
from tools.subsector import Subsector
from rich.console import Console
from enum import Enum

console = Console()

class Context:
    format: str

    def __init__(self, format: str) -> None:
        self.format = format


@click.group()
@click.option("--format", type=click.Choice(["table", "yaml"]), default="table", show_default=True, help="specify the output format")
@click.pass_context
def main(ctx, format):
    """Select tools for the Traveller5 Referee"""
    ctx.obj = Context(format)

@main.command()
@click.pass_context
@click.option("--extended/--abbreviated", show_default=True, help="whether to generate a full UWP or an abbreviated one")
def uwp(ctx, extended):
    """Generate a single UWP"""
    print(extended)
    uwp = UWP()
    console.print(uwp)

@main.command()
@click.pass_context
def subsector(ctx):
    """Generate a subsector"""
    subsector = Subsector()

    if ctx.obj.format == "table":
        from rich.table import Table
        table = Table()

        table.add_column("Position", justify="right")
        table.add_column("UWP", justify="right")

        for (pos, uwp) in subsector.worlds:
            table.add_row(pos, str(uwp))

        console.print(table)
    else:
        import yaml
        from rich.syntax import Syntax
        dump = yaml.dump({ "subsector":{ pos:uwp for (pos, uwp) in subsector.worlds }})
        syntax = Syntax(dump, "yaml", theme="ansi_dark")
        console.print(syntax)

main()
