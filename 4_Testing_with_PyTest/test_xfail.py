# Exercise: Skip Tests
# Using parameter strict=True

# Command: pytest -v 4_Testing_with_PyTest/test_xfail.py

import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
