"""
Converte JPY para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=145.00, help="Taxa de conversao de JPY para USD")
def jpy(preco, cambio):
    """Converte JPY para USD."""
    usd = preco * (1 / cambio)
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    jpy()
