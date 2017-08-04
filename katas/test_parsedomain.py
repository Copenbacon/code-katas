import pytest
from parsedomain import domain_name

def test_domain_simple_one():
	"""A simple test to see that the function works"""
	assert domain_name("http://google.com") == "google"


def test_domain_simple_two():
	"""A simple test to see that the function works"""
	assert domain_name("www.xakep.ru") == "xakep"


def test_domain_simple_three():
	"""A simple test to see that the function works"""
	assert domain_name("https://youtube.com") == "youtube"

