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
def cu():
    """Converte moedas"""
    pass


cu.add_command(usd)
cu.add_command(eur)
cu.add_command(gbp)
cu.add_command(chf)
cu.add_command(jpy)
cu.add_command(cad)
cu.add_command(aud)
cu.add_command(nzd)
cu.add_command(brl)
cu.add_command(hkd)


if __name__ == "__main__":
    cu()
