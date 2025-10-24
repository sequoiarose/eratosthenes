# file for testing 
from sievetools import *
import pytest

print("in test")
# things to test:
# - inputs are positive integers
# - slow and fast give the same result
# - fast is faster than slow
# - test a specific outcome is correct, e.g., factorization of 6

def test_input():
    return

def test_consistency():
    assert get_primes(55, "fast") == sieve_fast(55)

def test_consistency_fast():
    assert get_primes(55, "fast") == sieve_slow(55)

    