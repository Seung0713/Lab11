import unittest
from functions import *

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(7))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(8))

    def test_edge_case_zero(self):
        self.assertFalse(is_prime(0))

    def test_edge_case_one(self):
        self.assertFalse(is_prime(1))

    def test_large_prime(self):
        self.assertTrue(is_prime(101))

    def test_negative_number(self):
        self.assertFalse(is_prime(-5))

class TestRemoveVowels(unittest.TestCase):
    def test_regular_string(self):
        self.assertEqual(remove_vowels("hello"), "hll")  # e and o removed

    def test_uppercase_vowels(self):
        self.assertEqual(remove_vowels("AEIOU"), "")  # all vowels removed

    def test_mixed_case(self):
        self.assertEqual(remove_vowels("ApPlE"), "pPl")  # A and E removed

    def test_string_with_y(self):
        self.assertEqual(remove_vowels("yummy"), "ymmy")  # y is not a vowel

    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")  # no vowels to remove

if __name__ == '__main__':
    unittest.main()
