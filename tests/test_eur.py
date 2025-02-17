from click.testing import CliRunner
from cur import cur

run = CliRunner()


def test_calcula_conversao_eur_para_usd():
    res = run.invoke(cur, ["eur", "10"])
    assert res.output == "11.00 USD\n"


def test_calcula_conversao_eur_para_usd_com_opcao_cambio():
    res = run.invoke(cur, ["eur", "--cambio", "1.05", "10"])
    assert res.output == "10.50 USD\n"
