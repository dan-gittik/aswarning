import pytest

import aswarning


class MyWarning(Warning):
    pass


def test_aswarning(capsys):
    with pytest.warns(MyWarning) as record:
        with aswarning.as_warning('foo', MyWarning):
            raise ValueError('bar')
    warning = record[0].message.args[0].strip()
    assert warning.startswith('foo')
    assert warning.endswith('ValueError: bar')
