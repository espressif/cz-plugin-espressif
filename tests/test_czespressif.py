import re

from czespressif.czespressif import CzPluginEspressif


def strip_ansi_codes(text: str) -> str:
    """Strip ANSI color codes from a string for snapshot comparison."""
    ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def test_example(config, snapshot):
    """Testing the output returned by 'cz example' and comparing it with snapshot"""
    cze_config = CzPluginEspressif(config)
    example = strip_ansi_codes(cze_config.example())
    assert example == snapshot


def test_schema(config, snapshot):
    """Testing the output returned by 'cz schema' and comparing it with snapshot"""
    cze_config = CzPluginEspressif(config)
    schema = cze_config.schema()
    assert schema == snapshot


def test_info(config, snapshot):
    """Testing the output returned by 'cz info' and comparing it with snapshot"""
    cze_config = CzPluginEspressif(config)
    info = strip_ansi_codes(cze_config.info())
    assert info == snapshot
