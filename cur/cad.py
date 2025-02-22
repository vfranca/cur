"""
Converte CAD para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=1.34, help="Taxa de conversao de CAD para USD")
def cad(preco, cambio):
    """Converte CAD para USD."""
    usd = preco * (1 / cambio)
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    cad()
