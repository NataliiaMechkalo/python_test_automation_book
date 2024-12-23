# Home task 2
# Implement method overriding in a test automation context.
# Override a method in the child test class to customize the test execution.

class ExampleTestCase:
    def setUp(self):
        print("Setup complete")

    def runTest(self):
        print("Run")

    def tearDown(self):
        print("Cleanup complete")


class CustomTestExacution(ExampleTestCase):
    def run(self):
        print("Custom run")

exampleTestCase1 = CustomTestExacution()
exampleTestCase2 = CustomTestExacution()

exampleTestCase1.setUp()
exampleTestCase1.runTest()
exampleTestCase1.tearDown()

exampleTestCase2.setUp()
exampleTestCase2.runTest()
exampleTestCase2.tearDown()