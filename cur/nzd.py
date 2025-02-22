"""
Converte NZD para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=0.60, help="Taxa de conversao de HKD para USD")
def nzd(preco, cambio):
    """Converte NZD para USD."""
    usd = preco * cambio
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    nzd()
