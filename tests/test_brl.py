from click.testing import CliRunner
from cur import cur

run = CliRunner()


def test_calcula_conversao_brl_para_usd():
    res = run.invoke(cur, ["brl", "55"])
    assert res.output == "9.82 USD\n"
