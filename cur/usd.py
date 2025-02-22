"""
Converte USD para BRL
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=6.00, help="Taxa de conversao de USD para BRL")
def usd(preco, cambio):
    """Converte USD para BRL"""
    brl = preco * cambio
    click.echo("%.2f BRL" % brl)


if __name__ == "__main__":
    usd()
