from click.testing import CliRunner
from cur import cur

run = CliRunner()


def test_calcula_conversao_gbp_para_usd():
    res = run.invoke(cur, ["gbp", "10"])
    assert res.output == "12.83 USD\n"


def test_calcula_conversao_gbp_para_usd_com_opcao_cambio():
    res = run.invoke(cur, ["gbp", "--cambio", "1.25", "10"])
    assert res.output == "12.50 USD\n"
