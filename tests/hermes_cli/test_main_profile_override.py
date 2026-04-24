import os
import subprocess
import sys
from pathlib import Path


def test_profile_flag_sets_home_and_hermes_home(tmp_path):
    root = tmp_path / ".hermes"
    profile = root / "profiles" / "coder"
    (profile / "home").mkdir(parents=True)

    env = os.environ.copy()
    env["HERMES_HOME"] = str(root)
    env["HOME"] = str(root / "profiles" / "dev" / "home")

    code = """
import os, sys
sys.argv = ['hermes', '--profile', 'coder', 'profile']
import hermes_cli.main
print('HERMES_HOME=' + os.environ.get('HERMES_HOME', ''))
print('HOME=' + os.environ.get('HOME', ''))
"""
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        env=env,
        cwd=Path(__file__).resolve().parents[2],
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert f"HERMES_HOME={profile}" in lines
    assert f"HOME={profile / 'home'}" in lines
