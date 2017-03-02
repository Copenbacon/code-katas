"""Test Module for Anagrams.py."""
import pytest
from anagrams import anagrams

TEST_TABLE = [
    ('abba', ['aabb', 'abcd', 'bbaa', 'dada'], ['aabb', 'bbaa']),
    ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'], ['carer', 'racer']),
    ('a', ['a', 'b', 'c', 'd'], ['a']),
    ('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer'], ['ab', 'ba']),
    ('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa'], ['aabb', 'bbaa', 'abab', 'baba', 'baab']),
    ('big', ['gig', 'dib', 'bid', 'biig'], []),
]

@pytest.mark.parametrize("word, words, result", TEST_TABLE)
def test_anagrams(word, words, result)
    """Test the TEST_TABLE from CodeWars."""
    assert(anagrams(word, words) == result)
