#self = <failure_demo.TestSpecialisedExplanations object at 0xdeadbeef>
import unittest
class SomeClass:
	def test_eq_longer_list(self):
	       self.assertEqual [1, 2] == [1, 2, 3]


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def runTest(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50), 'incorrect default size')			#checks if the widget has size 50x50 

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')
'''

class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')
'''

    def tearDown(self):
        self.widget.dispose()
        self.widget = None


    @unittest.expectedFailure()				#decorator
    def testSomething():
	something = makeSomething()
	assert something.name is not None		#The test gives (F/./E) based on if the assertion is true or not. (F=Fail/False, . -pass/True, E -error in the test

@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):		#defs in the class
    def test_not_run(self):
        pass
