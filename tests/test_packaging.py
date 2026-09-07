from pathlib import Path
import tomllib


def test_setuptools_only_packages_runtime_module():
    with (Path(__file__).resolve().parents[1] / 'pyproject.toml').open('rb') as pyproject:
        config = tomllib.load(pyproject)

    assert config['tool']['setuptools']['packages']['find']['include'] == ['czespressif*']
