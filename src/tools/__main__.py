import rich_click as click
from rich.console import Console

from tools.subsector import Subsector
from tools.uwp import UWP

console = Console()


class Context:
    format: str

    def __init__(self, output_format: str) -> None:
        self.format = output_format


@click.group()
@click.option(
    "--format",
    type=click.Choice(["table", "yaml", "json"]),
    default="table",
    show_default=True,
    help="specify the output format",
)
@click.pass_context
def main(ctx, format):
    """Select tools for the Traveller5 Referee"""
    ctx.obj = Context(format)


@main.command()
@click.pass_context
@click.option(
    "--extended/--abbreviated",
    show_default=True,
    help="whether to generate a full UWP or an abbreviated one",
)
def uwp(ctx, extended):
    """Generate a single UWP"""
    uwp = UWP()
    console.print(uwp)


@main.command()
@click.pass_context
def subsector(ctx):
    """Generate a subsector"""
    worlds = Subsector().random()

    match ctx.obj.format:
        case "table":
            from rich.table import Table

            table = Table()

            table.add_column("Position", justify="right")
            table.add_column("UWP", justify="right")

            for pos, uwp in worlds:
                table.add_row(f"{pos[0]:02d}{pos[1]:02d}", str(uwp))

            console.print(table)
        case "yaml":
            import yaml
            from rich.syntax import Syntax

            dump = yaml.dump({"subsector": {pos: uwp for (pos, uwp) in worlds}})
            syntax = Syntax(dump, "yaml", theme="ansi_dark")
            console.print(syntax)
        case "json":
            import json
            from rich.syntax import Syntax

            dump = json.dumps(
                {
                    pos: {k: f"{v:X}" for (k, v) in uwp.__dict__.items()}
                    for (pos, uwp) in worlds
                },
                indent=4,
            )
            syntax = Syntax(dump, "json", theme="ansi_dark")
            console.print(syntax)


main()
