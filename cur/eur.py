"""
Converte EUR para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=1.10, help="Taxa de conversao de EUR para USD")
def eur(preco, cambio):
    """Converte EUR para USD."""
    usd = preco * cambio
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    eur()
