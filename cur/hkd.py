"""
Converte HKD para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=7.79, help="Taxa de conversao de HKD para USD")
def hkd(preco, cambio):
    """Converte HKD para USD."""
    usd = preco * (1 / cambio)
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    hkd()
