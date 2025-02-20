from click.testing import CliRunner
from cur.cur import cur

run = CliRunner()


def test_calcula_conversao_jpy_para_usd():
    res = run.invoke(cur, ["jpy", "300"])
    assert res.output == "2.07 USD\n"


def test_calcula_conversao_jpy_para_usd_com_opcao_cambio():
    res = run.invoke(cur, ["jpy", "--cambio", "152", "300"])
    assert res.output == "1.97 USD\n"
