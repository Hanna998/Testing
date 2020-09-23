def exp(a,b):
	return a**b

def test_answer():
   	assert exp(3,2) == 9
	assert exp(5,0) == 1
	assert exp(0,8) == 0
	assert exp(-2,2) == 4


