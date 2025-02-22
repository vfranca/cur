"""
Converte BRL para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=5.60, help="Taxa de conversao de BRL para USD")
def brl(preco, cambio):
    """Converte BRL para USD."""
    usd = preco * (1 / cambio)
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    brl()
