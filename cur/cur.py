"""
Aplicativo CLI para conversão de moedas
"""

import click
from cur.usd import usd
from cur.eur import eur
from cur.gbp import gbp
from cur.chf import chf
from cur.jpy import jpy
from cur.cad import cad
from cur.aud import aud
from cur.nzd import nzd
from cur.brl import brl
from cur.hkd import hkd


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
