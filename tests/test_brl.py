from click.testing import CliRunner
from cur import cur

run = CliRunner()


def test_calcula_conversao_brl_para_usd():
    res = run.invoke(cur, ["brl", "55"])
    assert res.output == "9.82 USD\n"


def test_calcula_conversao_brl_para_usd_com_opcao_cambio():
    res = run.invoke(cur, ["brl", "--cambio", "5.71", "55"])
    assert res.output == "9.63 USD\n"
