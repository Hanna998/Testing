import pytest

def division(a,b):
	return a/b

def test_answer():
	assert division(3,2) == 1.5   
	assert division(0,8) == 0
	assert division(-2,2) == -1

def test_zero_division():
	with pytest.raises(ZeroDivisionError):
		1 / 0


#	assert division(5,0) == ZeroDivisionError
#A Python 3-ban 1, a Python 2-ben 1.5 a helyes válasz

