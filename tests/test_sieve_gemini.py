import pytest
import numpy as np
import math
from sievetools import *

def test_sieve_nmax_10():
    """Tests sieve_slow for nmax = 10"""
    expected = [2, 3, 5, 7]
    assert sieve_slow(10) == expected

def test_sieve_nmax_30():
    """Tests sieve_slow for nmax = 30"""
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert sieve_slow(30) == expected

def test_sieve_nmax_2():
    """Tests the specific edge case of nmax = 2"""
    expected = [2]
    assert sieve_slow(2) == expected

def test_sieve_nmax_3():
    """Tests for nmax = 3, which should work correctly"""
    expected = [2, 3]
    assert sieve_slow(3) == expected

def test_sieve_nmax_100():
    """Tests a larger list of known primes (up to 100)"""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert sieve_slow(100) == expected_primes

# --- Tests for Expected Failures ---

def test_sieve_nmax_one_fails():
    """
    Tests for nmax = 1. 
    This test is expected to PASS because it asserts that
    an IndexError is raised, which is what the buggy function does.
    """
    with pytest.raises(IndexError):
        sieve_slow(1)

def test_sieve_nmax_zero_fails():
    """
    Tests for nmax = 0.
    This test also expects an IndexError.
    """
    with pytest.raises(IndexError):
        sieve_slow(0)

def test_sieve_nmax_negative_fails():
    """
    Tests for nmax = -5.
    This test also expects an IndexError.
    """
    with pytest.raises(IndexError):
        sieve_slow(-5)
