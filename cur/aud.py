"""
Converte AUD para USD
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=0.69, help="Taxa de conversao do AUD para o USD")
def aud(preco, cambio):
    """Converte AUD para USD."""
    usd = preco * cambio
    click.echo("%.2f USD" % usd)


if __name__ == "__main__":
    aud()
