import pytest
import repo.main


def test_help_cmd(capfd):
  with pytest.raises(SystemExit):
    repo.main._Main(["--help"])
  out, err = capfd.readouterr()
  assert "Usage: repo" in out
  assert err == ""