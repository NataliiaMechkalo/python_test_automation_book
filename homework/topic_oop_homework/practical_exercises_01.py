# Home task 1
# Write a TestCase class with methods for setup(), run(), and teardown().
# Create objects of the TestCase class to represent individual test cases.

class ExampleTestCase:
    def setUp(self):
        print("Setup complete")

    def runTest(self):
        print("run")

    def tearDown(self):
        print("Cleanup complete")


exampleTestCase1 = ExampleTestCase()
exampleTestCase2 = ExampleTestCase()

exampleTestCase1.setUp()
exampleTestCase1.runTest()
exampleTestCase1.tearDown()

exampleTestCase2.setUp()
exampleTestCase2.runTest()
exampleTestCase2.tearDown()