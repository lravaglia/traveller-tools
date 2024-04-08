import rich_click as click
from tools.uwp import UWP
from tools.subsector import Subsector
from rich.console import Console
from enum import Enum

console = Console()

class Format(str, Enum):
    TABLE = "table"
    YAML = "yaml"

class Context:
    format: Format

    def __init__(self, format: Format) -> None:
        self.format = format


@click.group()
@click.option("--format", type=click.Choice(Format), default=Format.TABLE)
@click.pass_context
def main(ctx, format):
    ctx.obj = Context(format)

@main.command()
def uwp():
    uwp = UWP()
    console.print(uwp)

@main.command()
@click.pass_context
def subsector(ctx):
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
