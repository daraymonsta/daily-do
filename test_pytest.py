import pytest

def test_add5():
  starting_number = 10.102645
  myval = starting_number+5
  assert myval == 16.102645, "test failed because " + str(starting_number) + "+5 is " + str(myval)
