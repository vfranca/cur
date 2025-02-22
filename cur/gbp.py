"""
Converte GBP para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=1.283, help="Taxa de conversao de GBP para USD")
def gbp(preco, cambio):
    """Converte GBP para USD."""
    usd = preco * cambio
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    gbp()
