"""
Aplicativo CLI para conversão de moedas
"""

import click
from usd import usd
from eur import eur
from gbp import gbp
from chf import chf
from jpy import jpy
from cad import cad
from aud import aud
from nzd import nzd
from brl import brl
from hkd import hkd


@click.group()
def cur():
    """Converte moedas"""
    pass


cur.add_command(usd)
cur.add_command(eur)
cur.add_command(gbp)
cur.add_command(chf)
cur.add_command(jpy)
cur.add_command(cad)
cur.add_command(aud)
cur.add_command(nzd)
cur.add_command(brl)
cur.add_command(hkd)


if __name__ == "__main__":
    cur()
