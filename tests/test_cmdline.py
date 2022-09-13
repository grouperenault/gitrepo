import repo.main


def test_help_cmd(capfd):
  repo.main._Main(["--help"])
  out, err = capfd.readouterr()
  assert "Usage: repo" in out
  assert err == ""