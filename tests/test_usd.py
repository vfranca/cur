from click.testing import CliRunner
from cur.cur import cur

run = CliRunner()


def test_calcula_conversao_usd_para_brl():
    res = run.invoke(cur, ["usd", "10"])
    assert res.output == "60.00 BRL\n"


def test_calcula_conversao_usd_para_brl_com_opcao_cambio():
    res = run.invoke(cur, ["usd", "--cambio", "5.71", "10"])
    assert res.output == "57.10 BRL\n"
