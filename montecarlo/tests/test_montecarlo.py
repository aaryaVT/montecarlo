"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo
import bitstring from BitString


def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules

import numpy as np
from ./bitstring import BitString 

def test_init_and_repr():
    b = BitString(4)
    assert repr(b) == "0000"
    assert len(b) == 4
    assert all(b.config == np.zeros(4, dtype=int))

def test_on_off():
    b = BitString(4)
    assert b.on() == 0
    assert b.off() == 4

    b.config = np.array([1, 0, 1, 0])
    assert b.on() == 2
    assert b.off() == 2

def test_eq():
    b1 = BitString(4)
    b2 = BitString(4)
    assert b1 == b2

    b1.config[0] = 1
    assert b1 != b2

def test_flip_site():
    b = BitString(4)
    b.flip_site(2)
    assert b.config[2] == 1
    b.flip_site(2)
    assert b.config[2] == 0

def test_integer():
    b = BitString(4)
    b.config = np.array([1, 0, 1, 1])  # binary 1011 → decimal 11
    assert b.integer() == 11

    b.config = np.array([1, 1, 1, 1])  # binary 1111 → decimal 15
    assert b.integer() == 15

def test_set_config():
    b = BitString(4)
    b.set_config([1, 0, 1, 1])
    assert all(b.config == np.array([1, 0, 1, 1]))

def test_set_integer_config():
    b = BitString(4)
    b.set_integer_config(11)  # decimal 11 → binary 1011
    assert all(b.config == np.array([1, 0, 1, 1]))

    b.set_integer_config(15)  # decimal 15 → binary 1111
    assert all(b.config == np.array([1, 1, 1, 1]))
