"""
Converte CHF para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=0.87, help="Taxa de conversao de CHF para USD")
def chf(preco, cambio):
    """Converte CHF para USD."""
    usd = preco * (1 / cambio)
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    chf()
